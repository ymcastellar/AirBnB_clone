#!/usr/bin/python3
"""Console - CMD

Returns:
    interactive cmd with prompt = "(hbnb)"
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for de CMD.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_empyline(self, line):
        """Overwrite new line method
        """
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            w = line.split(' ')
            if w[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(w) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(w[0], w[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            w = line.split(' ')
            if w[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(w) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(w[0], w[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation
            of all instances based or not on the class name.
        """
        if line != "":
            w = line.split(' ')
            lis = []
            if w[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                for k, obj in storage.all().items():
                    if type(obj).__name__ == w[0]:
                        lis.append(str(obj))
                        print(lis)
        else:
            for k, obj in storage.all().items():
                lis.append(str(obj))
                print(lis)

    def update(self, line):
        """ Prints all string representation
            of all instances based or not on the class name.
        """
        if len(line) == 0:
            print("** class name missing **")
            return False
        if line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(line) == 1:
            print("** instance id missing **")
            return False
        if len(line) == 2:
            print("** attribute name missing **")
            return False
        if len(line) == 3:
            try:
                type(eval(line[2])) != dict
            except NameError:
                print("** value missing **")
                return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
