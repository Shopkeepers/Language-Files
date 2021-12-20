<p align="center">
  <img src="https://github.com/Shopkeepers/Shopkeepers-Wiki/wiki/images/logos/shopkeepers_logo_small_with_text.png?raw=true" alt="Shopkeepers logo"/>
</p>

## Shopkeepers Translations

Language files for the Shopkeepers plugin. Consider contributing!

**BukkitDev Page**: https://dev.bukkit.org/projects/shopkeepers  
**Wiki**: https://github.com/Shopkeepers/Shopkeepers-Wiki/wiki  
**Translations** : https://github.com/Shopkeepers/Translations/  
**Issue Tracker**: https://github.com/Shopkeepers/Shopkeepers/issues  
**Discord Server**: https://discord.gg/d9NKd5z  
**Source code**: https://github.com/Shopkeepers/Shopkeepers/  

### Using these Language Files

* Click the folder that matches your version of the Shopkeepers plugin. Some versions of the Shopkeepers plugin had no changes to their language files, so there is no separate folder for them. In that case, simply pick the next lower version for which this repository contains language files.
* Pick the language file that matches your desired language. If there is no translation for your language yet, consider [contributing](https://github.com/Shopkeepers/Translations#contributing) one!
* Once you have opened a language file, click the `[Raw]` button in the top right, and then either copy and paste the contents of the language file to a new file on your computer, or use your browser's `Save page as...` (`Ctrl+S`) action to download the file.
* In order to then get the Shopkeepers plugin to use your downloaded language file, follow the [instructions inside the wiki](https://github.com/Shopkeepers/Shopkeepers-Wiki/wiki/Language-Files#using-custom-language-files).

### Contributing

In order to really be of use, **this repository depends on contributions** for languages other than the defaults. Feel encouraged to add new translations, update outdated translations, or suggest changes to existing translations.

To contribute:
* Fork this repository (`[Fork]` button in the top-right corner of this page): This creates your own personal copy of this repository.
* Inside your fork, add or edit a language file. This can be done [directly here on GitHub](https://help.github.com/en/articles/managing-files-on-github). In order to later get your changes accepted, be sure to follow the principles listed below.
* Once you are done with your changes, GitHub shows you an option to `commit` them: This saves the changes.
* [Create a `Pull Request`](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork): This creates a request to apply the changes from your fork to this base repository.
  * When creating the Pull Request, you might have to click the `[compare across forks]` button to be able to select your fork repository.
  * GitHub might have created a new 'branch' for your changes (more on those below). Be sure to select the correct `compare` branch, i.e. the branch inside your fork repository that contains the changes you want to apply to this base repository.
  * GitHub will show you a checkbox somewhere at the bottom whether you want to "Allow edits from maintainers". Consider enabling this option, because this will allow me to do minor edits directly to your changes and speed up the process of adding them to this repository.
  * Click the `[Create pull request]` button to create the Pull Request.

**Alternatively**, there are also buttons to add and edit files directly in this repository: When you use those, GitHub will automatically fork this repository for you, create a `patch-x` branch to store your changes, and afterwards offer you the option to create a Pull Request for your changes.

In order to get your changes accepted, **try to follow these principles**:
* Stick to the default coloring and formatting scheme of the messages, and of the language file itself.
* Do not include author or server names, advertisements, or links.
* When adding a new language file, follow the naming pattern outlined inside the [wiki](https://github.com/Shopkeepers/Shopkeepers-Wiki/wiki/Language-Files#using-custom-language-files).
* This can be ignored if you add or edit language files directly here on GitHub: Use the `UTF-8` encoding for your language file. Some text editors, like for example [Notepad++](https://notepad-plus-plus.org/), allow you to easily determine and change the encoding of your language file. Try to use `UTF-8` right from the beginning, because changing the file encoding in retrospect might break special characters.
* Prefer creating multiple Pull Requests for independent changes (e.g. when adding or making changes in different language files, or for different plugin versions). On GitHub, you can [create multiple `Branches`](https://help.github.com/en/articles/creating-and-deleting-branches-within-your-repository), which allows you to keep each of your independent changes separate, and later create individual Pull Requests for them.
  * When you added or edited a file and are about to commit the changes, GitHub offers you an option to create a new branch for these changes.
  * If you add or edit files directly inside this repository, without manually creating a fork first, GitHub will automatically create a fork with a new `patch-x` branch to store your changes. In this case, you can probably ignore this aspect and let GitHub handle it automatically for you.
* You may also suggest changes or alternatives for already existing translations, including the default translations. But please include an explanation as to why you think that these changes are necessary or useful. If your suggestions affect the default language files, they are either considered for the next version of Shopkeepers, or added as an alternative translation in this repository.
* See [the next section](https://github.com/Shopkeepers/Translations#updating-a-language-file) for additional notes on updating existing language files for newer plugin versions.

### Updating a Language File

With every update of the Shopkeepers plugin (if there have been changes to the default language files), a new folder is created that contains the default translations (english, and likely german since I speak that myself), as well as a `changelog` file that lists the language file changes for this plugin version.

Follow these steps and notes to update an already existing language file for a new plugin version:
* The old language file for the previous version has to stay intact: Do not edit the old language file, but instead create a new language file with the same name inside the folder for the new plugin version.
* Copy the contents of the old language file to this new langage file.
* Go through the list of changes inside the new version's `changelog` file and step-by-step apply these changes to the newly added language file.
* The `changelog` will often times only mention that some message has changed. In order to figure out what exactly has changed, you will need to compare the contents of the default (`en`) language file of the previous plugin version with the contents of the default language file of the new plugin version. There are some text comparisons tools that might help you with this, including online tools such as https://text-compare.com/

If you have questions or suggestions, [join the Discord Server](https://discord.gg/d9NKd5z) or [create an issue](https://github.com/Shopkeepers/Translations/issues/new).

### Thanks to [all contributors](AUTHORS.md)!
