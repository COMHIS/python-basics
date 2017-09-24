# Part 1 - Installing Python

As a first step, we will install a programming language, called Python, on your personal laptop [(students at University of Helsinki: What if I don’t have a laptop?)](./using_cubbli.md). There are all kinds of things to learn about programming languages and the concepts utilized in them, but we will skip those for now, and just focus on getting the environment running. The next step depends on the operating system that you are running. 

---

* **Windows:**
  1. download Python 3 installer from [python.org](https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe).
  2. Run the installer, and make sure to check the box saying “add Python 3.6 to path”
  3. The installer might ask you to change maximum length of path variable. Do that if it does so.
  4. You should be done now. To see if the installation was successfull go to part [“running python in terminal”](./python_terminal.md) in this assignment.
* **Linux (Ubuntu):**
  1. Test if you already have Python 3 installed by following the instructions at [“running python in terminal”](./python_terminal.md).
  2. If not, follow the instructions at [this askubuntu.com answer](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get).
* **Mac:**
  1. Test if you already have Python 3 installed by following the instructions at [“running python in terminal”](./python_terminal.md).
  2. If you don’t have Python 3 already installed, you can go about in two different ways:
    * SIMPLE (quite ok for now)
      * go to www.python.org, download the python 3.6.2 version from the main page
      * install it
      * you’re go
    * (NOT THAT) COMPLICATED (but useful in the long term)
      * Install XCode (a collection of software development tools for OS). You need XCode to install Homebrew.
      * Install Homebrew (OS software from handling software packages that automatically takes care of dependencies). With Homebrew you can easily install all kinds of software development packages.
      * Install python3 using Homebrew.
      * Full instructions to steps i-iii can be found [here](http://docs.python-guide.org/en/latest/starting/install3/osx/) or [here](http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html)  
      (steps Install Xcode and Homebrew and Install Python 3, not necessary to go the Virtual Environments yet)The instructions describe essentially the same steps.

---

## Python in Terminal

Make sure that you now have Python 3 installed by following the instructions [here](./python_terminal.md) and return back after finishing with those.

---

## Directory for your program

* Create a directory (also known as folder) for your project. This would typically be under your personal home directory. A typical structure for programming projects would be as follows: `home/projects/name_of_project`
* Use terminal to navigate to your project directory:
  * Terminal usually opens in your home directory
  * We can see a list of the contents of the directory we currently are in terminal by typing `dir` (in Windows) or `ls` (in Linux or MacOS)
  * To move into a subdirectory of the current directory type `cd [name of the directory]` eg. `cd dhprogramming1` 
  * To move one step back type `cd ..`

---

## Hello World!

Now that we have Python installed let’s create the classic first program, called “Hello World”. The reason for that name becomes obvious soon.

* Open a text editor that saves the text in plain text format (meaning text without any formatting). Word or OpenOffice isn’t a good choice here, but the following programs are (among many others):
  * **Windows:** Notepad
  * **Linux:** Gedit
  * **Mac:** TextEdit (you have to go into plain text mode by following the instructions [here](https://www.tekrevue.com/tip/textedit-plain-text-mode/))
* Write the following line of code on the first row in the text file, and add a blank line below that (all python programs finish with one empty row).  
```python
print("Hello World!")

```
* Save the text in a file named `helloworld.py` in the project directory you created. 
* Open terminal like you previously did and navigate to the project directory that you created earlier.
* Type command `python3 helloworld.py` in terminal to see your first program in action.
* If all goes well you should see the text `Hello World!` appear in the terminal.

---

## Finding answers and moving on

* If something went wrong come to our course Slack at *[dhintros.slack.com](https://dhintros.slack.com)* and describe the problem. Feel free to offer advice to your fellow students struggling with problems that you were able to solve. Also, feel free to use google to look for answers if you get stuck. Strong googling skills are at least 50% of all programming.
* After you’ve got the code working try modifying it to print something else.
* You can also try playing around with in Python terminal: run the command `python3` in terminal, and you should see the interactive version of Python coming up. Type the previous code in, and press enter to execute it.
  * To leave the interpreter, type `quit()`.
