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

### Using these translations

* Click the folder that matches your version of the Shopkeepers plugin. Some versions of the Shopkeepers plugin had no changes to their language files, so there is no separate folder for them. In that case, simply pick the next lower version for which this repository contains language files.
* Pick the language file that matches your desired language. If there is no translation for your language yet, consider [contributing](https://github.com/Shopkeepers/Translations#contributing) one!
* Once you have opened a language file, click the `[Raw]` button in the top right, and then either copy and paste the contents of the language file to a new file on your computer, or use your browser's `Save page as...` (`Ctrl+S`) action to download the file.
* In order to then get the Shopkeepers plugin to use your downloaded language file, follow the [instructions inside the wiki](https://github.com/Shopkeepers/Shopkeepers-Wiki/wiki/Language-Files#using-custom-language-files).

### Contributing

In order to really be of use, **this repository depends on contributions** for languages other than the defaults. Feel encouraged to add new translations, update outdated translations, or suggest changes of existing translations.

Simply fork the project (this creates your own personal copy of this repository), add or edit a language file there, and then [create a `Pull Request`](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork). You can also [add and edit files directly here on Github](https://help.github.com/en/articles/managing-files-on-github) inside the browser: Github will then automatically fork the repository for you and offer you the option to create a Pull Request for your changes.

In order to get your changes approved **try to follow these principles**:
* Prefer creating multiple Pull Requests for independent changes (eg. adding or making changes in different language files and for different plugin versions). On Github, you can [create different `Branches`](https://help.github.com/en/articles/creating-and-deleting-branches-within-your-repository), which allows you to keep each of your independent changes separate. If you [add and edit files directly here on Github](https://help.github.com/en/articles/managing-files-on-github), Github will already automatically create a fork with a new `patch-x` branch for your changes. So unless you want to make changes to your edits afterwards, you can probably ignore this aspect and let Github handle it automatically for you.
* When you create the Pull Request for your changes, Github will show you a checkbox somewhere at the bottom whether you want to "Allow edits from maintainers". Consider enabling this option, because this will allow me to do minor edits directly to your changes and speed up the process of adding your changes to this repository.
* Stick to the default coloring and formatting scheme of the messages, and of the language file itself.
* Do not include author or server names, advertisements, or links.
* Use the `UTF-8` encoding for your language file. For example, the text editor [Notepad++](https://notepad-plus-plus.org/) allows you to easily determine and change the encoding of your language file. Try to use `UTF-8` right from the beginning, because changing the file encoding in retrospect might break special characters. If you edit language files directly here on Github, you can ignore this aspect.
* See [the next section](https://github.com/Shopkeepers/Translations#updating-a-translation) for notes on updating existing translations for newer plugin versions.
* You may also suggest changes or alternatives for already existing translations, including the default translations. But please include some reasoning on why you think that these changes are required. If your suggestions affect the default language files, they are then either considered for the next version of Shopkeepers, or added as an alternative translation in this repository.

### Updating a translation

With every update of the Shopkeepers plugin (if there have been changes to the default language files), a new folder is created containing the default translations (english, and likely german since I speak that myself), as well as a `changelog` file that lists the language file changes for this plugin version.

Follow these steps and notes to update an already existing language file for a new plugin version:
* The old language file for the previous version has to stay intact: Do not edit the old language file, but instead create a new language file with the same name inside the folder for the new plugin version.
* Copy the contents of the old language file to this new langage file.
* Go through the list of changes inside the new version's `changelog` file and step-by-step apply these changes to the newly added language file.
* The `changelog` will often times only mention that some message has changed. In order to figure out what exactly has changed, you will need to compare the contents of the default (`en`) language file of the previous plugin version with the contents of the default language file of the new plugin version. There are some text comparisons tools that might help you with this, including online tools such as https://text-compare.com/

If you have questions or suggestions, [join the Discord Server](https://discord.gg/d9NKd5z) or [create an issue](https://github.com/Shopkeepers/Translations/issues/new).

### Thanks to [all contributors](authors.md)!
