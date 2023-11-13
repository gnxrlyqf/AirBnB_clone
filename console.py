#!/usr/bin/python3
"""Defines HBNB command interpreter class"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class

    Attributes:
        prompt (str): custom prompt
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "City",
        "Amenity",
        "Place",
        "State",
        "Review"
    }

    def strtok(self, args):
        pattern = r'(\'[^\']*\'|"[^"]*"|\S+)'
        result = re.findall(pattern, args)
        output = []
        for token in result:
            if token[0] == token[-1] == '"':
                output.append(token[1:-1])
            else:
                output.append(token)
        return output

    def do_quit(self, arg):
        """Quit command to exit the programl"""
        return True

    def do_EOF(self, arg):
        """EOF signal triggers exit"""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        create new class and print id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = self.strtok(arg)
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                new = eval(args[0])()
                print(new.id)
                storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id>
        print dictionary representation of an object
        """
        if arg:
            args = self.strtok(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            if not "{}.{}".format(args[0], args[1]) in objects.keys():
                print("** no instance found **")
            else:
                print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        deletes an object
        """
        if arg:
            args = self.strtok(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif not args[0] in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            if not "{}.{}".format(args[0], args[1]) in objects.keys():
                print("** no instance found **")
            else:
                del objects["{}.{}".format(args[0], args[1])]
                storage.save()

    def do_all(self, arg):
        """Usage: all, all <class>
        lists all objects, or all objects of a class
        """
        storage.reload()
        objects = storage.all()
        if len(arg) == 0:
            print([str(val) for val in objects.values()])
        elif len(arg) > 0:
            if arg not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(objects[k]) for k in objects.keys() if arg in k])

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute> <value>
        updates or adds an attribute to an object
        """
        if arg:
            args = self.strtok(arg)
        storage.reload()
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif not args[0] in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not "{}.{}".format(args[0], args[1]) in objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = objects["<{}>.{}".format(args[0], args[1])]
            setattr(instance, args[2], args[3][1:-1])
            instance.save()

    def emptyline(self):
        """Empty line (do nothing)"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
