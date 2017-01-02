## Process checker
Checks processes running and relaunches if they're not running.. should of course never happen!

### Installation
This program uses Python in a virtual environment.

First change directory to the folder then set up a virtual environment

```
$ cd path/to/folder
$ virtualenv venv
```

Then activate the virtual environment:

```
$ source venv/bin/activate
```

Install dependencies using pip:

```
$ pip install -r requirements.txt
```

The program can now run:
```
$ python process_checker.py
```
