## Terminal / Console:

Terminal (or console) is a tool for running commands on the computer in an “old school” way. It looks something like this:

![Screenshot of Ubuntu Terminal](./terminal.jpg "Terminal in Ubuntu Linux")

When these instructions tell you to type something the terminal, the expectation is that you’ll press enter after typing in the command.

**Note:** The terminal environment can be a bit confusing when you first start using it. Eventually it will become second nature and a powerful tool, so bear with it.

**Note:** We'll be operating in two different terminal environments here. The first one is your operating system level, where you create and navigate directories and start Python to run your scripts. On that level the row where you type your commands looks a bit like this `C:\Users\mmeikal\> ▂` (windows) or this `mmeikal@rancomp-1:/home/local/mmeikal$ █` (linux, mac). On the other hand, when you are running Python inside the terminal the line for commands looks like this `>>> ▂`. These two environments have different sets of commands, and the commands for one don't work in the other.

---

Let’s test and make sure that the Python interpreter works/exists:

---

1. Open the terminal (follow the instructions for your operating system):
  * **Linux** (Cubbli):
    * Menu -> Terminal
    * or: bottom row: Terminal-icon
    * or: Ctrl+Alt+t
  * **Windows**:
    * Start -> Command Prompt (or Komentokehote)
    * or: Press Windows+R to open “Run” box. Type “cmd” and then click “OK” to open Command Prompt.
  * **Mac**:
    * Open the Console command line tool from Applications->Utilities->Console
2. Type `python3` (or `python`, see below ...)
  * You should see something like this:  
```
Python 3.4.3 (default, Nov 17 2016, 01:08:31)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
  * If nothing happens, try typing just `python`. Some installers use this name for the python executable.
  * Leave Python (now running in your terminal) by typing `quit()`. You are back to the "normal" terminal environment.
  * You can close the terminal window whenever you want. Nothing will break.
  * You can also close the terminal with the `exit` -command. This will close the terminal window.
