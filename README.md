# CLI-Todo
A command line interface to manage your todo lists. This Script is written as a part of CoronaSafe Engineering Fellowship Test Problem by Pupilfirst in the Python.

### _Author : Lekha Shanthini_

## Getting started
1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command

`(python3 --version)`
This should output some information on the installed Python version.

2. The code is written in todo.py file.

3. The todo app can be executed by running the following command from the terminal.

__On Windows__:

`(todo.bat)`

##Run Automated Tests
1. Install Node.js: You need to have npm installed in your computer for this problem. It comes with Node.js and you can get it by installing Node from https://nodejs.org/en/

2. Run npm install to install all dependencies

3. Create symbolic link to the executable file

__On Windows__:

`(mklink todo todo.bat)`
Note: This is a mandatory step else you've to use todo.bat instead of todo in the Command Prompt in Windows OS.

Now run npm test and you will see all the tests passing one by one.
