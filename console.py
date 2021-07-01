#!/usr/bin/python3
"""console"""

import cmd
from models.base_model import BaseModel
import models
import models.engine.file_storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

clss_list = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """HBNBcosole"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Ctrl D command to exit the program"""
        return True

    def emptyline(self):
        """command added to avoid that an empty
        line + ENTER executes anything
        """
        return cmd.Cmd.postloop(self)

    def do_create(self, cmds):
        """
        creates a new instance of a class
        """
        commands = cmds.split(' ')
        if not commands[0]:
            print("** class name missing **")
        elif commands[0] not in clss_list:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            instance.save()

    def do_show(self, cmds):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        commands = cmds.split(' ')
        if len(commands) > 1:
            key = commands[0] + '.' + commands[1]
        if not commands[0] or len(commands) == 1:
            print("** class name missing **")
        elif commands[0] not in clss_list:
            print("** class doesn't exist **")
        elif not commands[1]:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            print("{}".format(models.storage.all()[key]))

    def do_destroy(self, cmds):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        commands = cmds.split(' ')
        if len(commands) > 1:
            key = commands[0] + '.' + commands[1]
        if not commands[0] or len(commands) == 1:
            print("** class name missing **")
        elif commands[0] not in clss_list:
            print("** class doesn't exist **")
        elif not commands[1]:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            models.storage.all().pop(key)
            models.storage.save()

    def do_all(self, cmds):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        tmp_list = []
        commands = cmds.split(' ')
        if commands[0]:
            if commands[0] not in clss_list:
                print("** class doesn't exist **")
            else:
                for key in models.storage.all().keys():
                    if str(commands[0]) in key:
                        tmp_list.append(str(models.storage.all()[key]))
                print(tmp_list)
        else:
            for key in models.storage.all().keys():
                try:
                    tmp_list.append(str(models.storage.all()[key]))
                except:
                    pass
            print(tmp_list)

    def do_update(self, cmds):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute(save the change into the JSON file)
        """
        commands = cmds.split(' ')
        if len(commands) > 1:
            key = commands[0] + '.' + commands[1]
        if not commands[0] and len(commands) == 1:
            print("** class name missing **")
        elif commands[0] not in clss_list:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        elif len(commands) < 3:
            print("** attribute name missing **")
        elif len(commands) < 4:
            print("** value missing **")
        else:
            setattr (models.storage.all()[key], commands[2], str(commands[3]))
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()