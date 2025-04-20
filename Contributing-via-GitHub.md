# Contributing via GitHub

To contribute via Github:
* Fork this repository (`[Fork]` button in the top-right corner of this page): This creates your own personal copy of this repository.
* Inside your fork, [select the branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/viewing-branches-in-your-repository) that matches the plugin version you want to add or edit a language file for.
* Add or edit a language file. This can be done [directly here on GitHub](https://help.github.com/en/articles/managing-files-on-github). In order to later get your changes accepted, be sure to follow the principles listed below.
* Once you are done with your changes, GitHub shows you an option to `commit` them: This saves the changes.
* [Create a `Pull Request`](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork): This creates a request to apply the changes from your fork to this base repository.
  * When creating the Pull Request, you might have to click the `[compare across forks]` button to be able to select your fork repository.
  * GitHub might have created a new branch for your changes. Be sure to select both the correct `base` branch (the branch inside this base repository you want to apply your changes to), and the correct `compare` branch (the branch inside your fork repository that contains your changes).
  * GitHub will show you a checkbox somewhere at the bottom whether you want to "Allow edits from maintainers". Consider enabling this option, because this will allow me to do minor edits directly to your changes and speed up the process of adding them to this repository.
  * Click the `[Create pull request]` button to create the Pull Request.

**Alternatively**, there are also buttons to add and edit files directly in this repository: When you use those, GitHub will automatically fork this repository for you, create a `patch-x` branch to store your changes, and afterwards offer you the option to create a Pull Request for your changes.

Prefer creating multiple Pull Requests for independent changes (e.g. when adding or making changes in different language files, or for different plugin versions). On GitHub, you can [create multiple "branches"](https://help.github.com/en/articles/creating-and-deleting-branches-within-your-repository), which allows you to keep each of your independent changes separate, and later create individual Pull Requests for them.
* When you added or edited a file and are about to commit the changes, GitHub offers you an option to create a new branch for these changes.
* If you add or edit files directly inside this repository, without manually creating a fork first, GitHub will automatically create a fork with a new `patch-x` branch to store your changes. In this case, you can probably ignore this aspect and let GitHub handle it automatically for you.