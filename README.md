# AirBnB_clone

![hbnb](https://i.imgur.com/44u0pXG.png)

## Table of Contents

* [Description](#description)
* [Requirements](#requirements)
* [File Structure](#file-structure)
* [Usage](#usage)
* [Examples](#examples)
* [Authors](#authors)

## Description

**hbnb** is a clone of the web application AirBnB. This project will be constructed in multiples phases. In this phase we created a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

## Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## File Structure

* [AUTHORS](AUTHORS) - list of contributor
* [console.py](console.py) - command interpreter
  * `do_create` - create a new instance of a class
  * `do_show` - prints string representation of an instance based on class name and id
  * `do_all` - prints all string representation of all instances based or not on the class name
  * `do_destroy` - deletes an instance based on the class name and id
  * `do_update` - updates an instance based on the class name and id by adding or updating attribute
  * `emptyline` - ensures that hitting 'enter' will not remember the last command
  * `do_quit` - quit program
  * `do_EOF` - exit at end of file
* [file_storage.py](/models/engine/file_storage.py) - class FileStorage
  * `all` - returns the dictionary __objects
  * `new` - sets in __objects the obj with key <obj class name>.id
  * `save` - serializes __objects to the JSON file (path: __file_path)
  * `reload` - deserializes the JSON file to __objects
* [base_model.py](/models/base_model.py) - defines all common attributes/methods for other classes
  * `__init__` - initialize instance attributes
  * `__str__` - creates formatted string representation of instance
  * `__repr__` - returns string representation of instance
  * `save` - updates public instance attribute updated_at with current datetime
  * `to_dict` - creates a dictionary containing all keys/values of `__dict__` of the instance
* [user.py](/models/user.py) - class User
* [city.py](/models/city.py) - class City
* [state.py](/models/state.py) - class State
* [place.py](/models/place.py) - class Place
* [review.py](/models/review.py) - class Review
* [amenity.py](/models/amenity.py) - class Amenity
* [`__init__.py`](/models/__init__.py) - initialization code for Python package models
* [tests](/tests/) - unit test files

### Unit Testing
```python3 -m unittest discover tests```

## Execution
1. git clone https://github.com/Ang3l1t0/AirBnB_clone.git 
## Usage Examples
### Interactive Mode

```c
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

```c
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Authors
* Angel Palma | [GitHub](https://github.com/Ang3l1t0)) | [Twitter](https://twitter.com/Ang3lp)
* Yoyman Castellar | [GitHub](https://github.com/ymcastellar) | [Twitter](https://twitter.com/CastellarYoyman)
