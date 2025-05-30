# Contributing

In order to really be of use, **this repository depends on contributions** for languages other than the defaults. Feel encouraged to add new translations, update outdated translations, or suggest changes to existing translations.

To send me your translated language file either:
* Create an issue and attach (drag-and-drop) the language file there, or upload it somewhere else (e.g. https://pastebin.com/) and send me a link to it. Be sure to mention which plugin version your language file is meant for.
* Send me your translated language file via [Discord](https://discord.gg/d9NKd5z).
* If you are familiar with Git and GitHub, create a Pull Request. If you want to learn about how to contribute via GitHub, I try to explain the process [here](Contributing-via-GitHub.md).

In either case, be sure to follow the **contribution guidelines** mentioned below.

If you have any questions or suggestions, [join the Discord Server](https://discord.gg/d9NKd5z) or [create an issue](https://github.com/Shopkeepers/Language-Files/issues/new).

## Contribution Guidelines

In order to get your changes accepted, follow these principles:
* Check if there already exists a language file for your language and consider updating the existing file instead of adding your own variant.
* Test your language file at least once and make sure that the plugin can load it.
* Stick to the default coloring and formatting scheme of the messages, and of the language file itself.
* Do not include author names, server names, advertisements, or links.
* When adding a new language file, follow the naming pattern `language-<languageCode>.yml`.
* When you create a new language file outside of GitHub: Use the `UTF-8` encoding for your language file. Some text editors, like for example [Notepad++](https://notepad-plus-plus.org/), allow you to easily determine and change the encoding of your language file. Try to use `UTF-8` right from the beginning, because changing the file encoding in retrospect might break special characters.
* You may also suggest changes or alternatives for already existing translations, including the default translations. But please include an explanation as to why you think that these changes are necessary or useful. If your suggestions affect the default language files, they are either considered for the next version of Shopkeepers, or added as an alternative translation in this repository.
* See the section on [Updating a Language File](https://github.com/Shopkeepers/Language-Files#updating-a-language-file) for additional notes on updating existing language files for newer plugin versions.

## Updating a Language File

With every update of the Shopkeepers plugin, if there have been changes to the default language files:
* A new branch is created for this plugin version. This branch initially only contains the default language files (english, and likely german since I speak that myself).
* The [`CHANGELOG`](CHANGELOG.md) is updated: This file roughly summarizes the language file changes of each plugin version.

Follow these steps to update an already existing language file for a new plugin version:
* The old language file inside the branch of the previous version has to stay intact: Do not edit the old language file, but instead create a new language file with the same name inside the branch of the new plugin version.
* Copy the contents of the old language file (from the branch of the previous version) to this new langage file (inside the branch of the new plugin version).
* Go through the list of changes inside the [`CHANGELOG`](CHANGELOG.md) file and apply them step-by-step to the newly added language file.  
However, the changelog will often times only mention that some messages have changed. In order to figure out what exactly has changed, you will need to compare the contents of the default language file (`en-default`) of the previous plugin version with the contents of the default language file of the new plugin version. This can be achieved in the following ways:
  * Open the compare page [`https://github.com/Shopkeepers/Language-Files/compare`](https://github.com/Shopkeepers/Language-Files/compare) and select the two branches of the two plugin versions you want to compare. At the bottom of the comparison page, GitHub will then list all files that have changed, and all the lines that have changed within each of these files. Search for the default `en-default` language file to inspect its changes.
  * Alternative 1: Select the default `en-default` language file inside the branch of the latest plugin version, and then click the `[History]` button in the top-right corner of the page. This will bring up the commit history of this file. Select the commit for the latest plugin version update: This will visualize all the lines that have changed compared to the previous version of this file.
  * Alternative 2: Use some external text comparison tool like https://text-compare.com/.

## Thank you to [all contributors](CONTRIBUTORS.md)!