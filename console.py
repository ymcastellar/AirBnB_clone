#!/usr/bin/python3
"""Console - CMD

Returns:
    interactive cmd with prompt = "(hbnb)"
"""
import cmd
import shlex
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

    def emptyline(self):
        """Overwrite new line method
        """
        pass

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
        lis = []
        if line != "":
            w = line.split(' ')
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

    def do_update(self, line):
        """ Prints all string representation
            of all instances based or not on the class name.
        """
        if not line:
            print("** class name missing **")
            return

        w = shlex.split(line)
        if w[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(w) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, value in obj.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == w[0] and ob_id == w[1].strip('"'):
                    if len(w) == 2:
                        print("** attribute name missing **")
                    elif len(w) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, w[2], w[3].strip('"'))
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
