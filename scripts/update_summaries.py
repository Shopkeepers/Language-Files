import os
import re
import yaml
from collections import defaultdict
from packaging.version import parse as parse_version
from git import Repo

# === Configuration ===
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_DIR = "lang"
EN_DEFAULT = "en-default"
EN_DEFAULT_FILE = f"language-{EN_DEFAULT}.yml"
LANGUAGE_FILE_URL = "https://github.com/Shopkeepers/Language-Files/blob/{version}/lang/language-{lang_code}.yml"
README_TEMPLATE_FILE = os.path.join(REPO_ROOT, "templates", "README.md")

# === Helper Functions ===
def extract_language_code(filename):
    match = re.match(r"language-(.+)\.yml", filename)
    return match.group(1) if match else None

def flatten_yaml(data):
    flat = {}
    def recurse(d, prefix=''):
        if isinstance(d, dict):
            for k, v in d.items():
                recurse(v, prefix + k + '.')
        elif isinstance(d, list):
            flat[prefix[:-1]] = d
        else:
            flat[prefix[:-1]] = d
    recurse(data)
    return flat

def compare_language_files(old_dict, new_dict):
    missing = []
    outdated = []
    obsolete = []

    for key in new_dict:
        if key not in old_dict:
            missing.append(key)
        elif old_dict[key] != new_dict[key]:
            outdated.append(key)

    for key in old_dict:
        if key not in new_dict:
            obsolete.append(key)

    return missing, outdated, obsolete

# === Main Logic ===
def build_language_table():
    repo = Repo(REPO_ROOT)
    assert not repo.bare

    # Get all version branches sorted from highest to lowest
    # Note: repo.heads does not work in Github workflows.
    branches = [branch.name.replace("origin/", "") for branch in repo.remotes.origin.refs if branch.name.startswith("origin/v")]
    versions = sorted(branches, key=parse_version, reverse=True)

    # Parse en-default
    en_files = {}
    for version in versions:
        try:
            blob = repo.git.show(f"origin/{version}:{LANG_DIR}/{EN_DEFAULT_FILE}")
            en_files[version] = flatten_yaml(yaml.safe_load(blob))
        except Exception:
            raise RuntimeError(f"Version {version}: Failed to load {EN_DEFAULT_FILE}!") from e

    latest_version = versions[0]
    latest_en = en_files[latest_version]

    # Collect available language files per version
    lang_versions = defaultdict(set)
    lang_files = defaultdict(dict)

    for version in versions:
        try:
            tree = repo.git.ls_tree("-r", f"origin/{version}", f"{LANG_DIR}/")
            for line in tree.splitlines():
                _, _, _, path = line.split()
                if not path.endswith(".yml"):
                    raise RuntimeError(f"Version {version}: Unexpected file {path}");

                filename = os.path.basename(path)
                lang_code = extract_language_code(filename)
                if not lang_code:
                    raise RuntimeError(f"Version {version}: Failed to extract language code from file {path}!")

                lang_versions[lang_code].add(version)

                try:
                    blob = repo.git.show(f"origin/{version}:{path}")
                    lang_files[lang_code][version] = flatten_yaml(yaml.safe_load(blob))
                except Exception as e:
                    raise RuntimeError(f"Version {version}: Failed to load language file {path}!") from e
        except Exception as e:
            raise RuntimeError(f"Version {version}: Error") from e

    # Generate markdown table
    header = "| Language | Available Versions | Completeness | Missing | Outdated | Obsolete |\n"
    header += "|----------|--------------------|--------------|---------|----------|----------|\n"
    rows = []

    for lang_code in sorted(lang_versions.keys()):
        sorted_lang_versions = sorted(lang_versions[lang_code], key=parse_version, reverse=True)
        latest_lang_version = sorted_lang_versions[0]
        latest_lang = lang_files[lang_code][latest_lang_version]

        # Missing/obsolete: Compare latest translation to latest en
        missing, _, obsolete = compare_language_files(latest_lang, latest_en)

        # Outdated: Compare en at language's version vs. en at latest version
        outdated = []
        if lang_code != EN_DEFAULT:
            from_en = en_files.get(latest_lang_version)
            if from_en:
                _, outdated, _ = compare_language_files(from_en, latest_en)

        # If number of issues exceeds number of keys, we show "0%"
        total_issues = len(missing) + len(outdated) + len(obsolete)
        total_keys = len(latest_en)
        completeness = max(0.0, 100.0 * (1 - total_issues / total_keys) if total_keys else 100.0)

        version_links = " ".join(
            f"[{f'**{version}**' if version == latest_version else f'{version}'}]({LANGUAGE_FILE_URL.format(version=version, lang_code=lang_code)})"
            for version in sorted_lang_versions
        )

        row = f"| {lang_code} | {version_links} | {completeness:.0f}% | {len(missing)} | {len(outdated)} | {len(obsolete)} |"
        rows.append((lang_code, sorted_lang_versions[0], row)) # Track code and version for sorting

    # Sort rows by:
    # 1. Put en first
    # 2. Then by latest available language version (desc)
    rows.sort(key=lambda x: (x[0] == EN_DEFAULT, parse_version(x[1])), reverse=True)

    return header + "\n".join(row for _, _, row in rows)

def update_readme(language_table):
    # Read the template
    with open(README_TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholder
    readme_content = template.replace("{LANGUAGES}", language_table)

    # Write the final README
    with open(os.path.join(REPO_ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("Readme updated!")

if __name__ == "__main__":
    language_table = build_language_table()
    update_readme(language_table)
    # TODO Automatically generate and update the contributors file
