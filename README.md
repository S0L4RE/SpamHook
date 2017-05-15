# SpamHook
A trolling utility that spams Discord webhooks with a message of the user's choice.

## IMPORTANT NOTICE REGARDING SPAMHOOK'S END OF LIFETIME:

### SpamHook v2 will be the last major version of SpamHook that will be released. Minor updates and support will still be offered. The reason behind this is that raids on Discord have become less and less fun, especially with the recent release of Audit Logs and the upcoming (at the time of this writing) release of the Report button. So, I felt as if SpamHook needed to be left at v2.

### **However, don't get your hopes down too soon!** If enough support and demand is shown for a SpamHook v3, it will be done. In C# because why not. Hexexpeck is also working on a few other cool things, including but not limited to:

- Choco Discord Bot (Hexexpeck's own Discord bot, replacement for Hex/HexagonBot made in JavaScript using the discord.js library)
- SplatPack (more info soon:tm: ;)
- An attempt at making some sort of minimal REST client because the current options are shite imho

## How to get?
Visit the [Releases](https://github.com/Hexexpeck/SpamHook/releases) page on GitHub.
The SpamHook Alpha Testing Program is officially discontinued with the final release (v2) of SpamHook.

## Compiling the Windows EXE
- Install Python 3.5
- Install Git
- Clone this repository using git
```
git clone https://github.com/Hexexpeck/SpamHook
```
- Get PyInstaller via Python's pip package manager
```
pip3 install pyinstaller
```
- Run the following command to build the Windows executable.
```
pyinstaller --clean --log-level DEBUG --onefile --name SpamHook -i more_spam.ico --uac-admin --osx-bundle-identifier com.hexexpeck.spamhook.revisiondos SpamHook-v2.py
```
Building the Windows executable will take some time, so be patient. You'll know its complete when the command completes and you regain access to your command window.
