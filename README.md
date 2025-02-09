# Tiny Python Projects

## Hello World !

### Setup Concideration

Python scripts accept shebang at their top `#!/usr/bin/env python3`, this will indicate which programm to use when the file is executed.

The above shebang will work on any machine if python3 is installed and present in the `env` variable.

```shell
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ env python3
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(.tpp) 
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ which python3
/c/Users/JKESSOUS/AppData/Local/Microsoft/WindowsApps/python3
```

We could use a specific shabang to instruct the python interpreter to use like so `#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3` but it would be specific to this computer only.

Because we added a shebang to the top line of our programm, we can now execute it directly and let the OS figure out how to. The only thing to do is to make the file an executable with 

```shell
chmod +x hello.py
```

We can now run the programm directly from terminal as so:

```shell
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ ./hello.py 
Hello, World!
```

If i where to move `hello.py` in my binaries folder, i could run it from anywhere in the computer without even specifying the path toward the executable.

A common way to achieve the same result is to create a ``bin`` directory in the user home repo and to add it to the `$PATH`:

```shell
$ mkdir ~/bin
$ cp 01_hello/hello.py ~/bin
$ PATH=~/bin:$PATH
$ which hello.py
/home/runner/bin/hello.py

```

### Arguments

The `argparse` module provides tool for parsing arguments of our CLI.

We can tell the CLI to accept a **positionnal argument** like so

```python
#!/usr/bin/env python3
# Purpose: Say hello
 
import argparse
 
parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')

```

Positionnal arguments are mandatory and programm won't run if not provided.

We can also accept optional arguments (defined with a dash) along with their default value as follow:

```python
#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')

```

Those arguments can be defined with a *short* and a *long* named.

```shell

$ ./hello.py 
Hello, World!
(.tpp) 
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ ./hello.py -n toto
Hello, toto!
(.tpp) 
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ ./hello.py --name toto
Hello, toto!
(.tpp) 
JKESSOUS@L-5CG3463Q90 MINGW64 ~/Documents/Tiny_Python_Project/01_hello (main)
$ ./hello.py --name=toto
Hello, toto!

```

### Makefile

Makefiles are used along with the `make` util to define custom receipe.

```shell
$ cat Makefile
.PHONY: test

test:
   pytest -xv test.py
```

