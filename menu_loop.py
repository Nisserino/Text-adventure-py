import cmd
import json, os
import file_handler as fh


class Main_menue_loop(cmd.Cmd):
    intro = ""
    prompt = "(Player): "

    def do_saves(self, arg):
        Choose_class().cmdloop()

    def do_start(self, arg):
        'Initialize a new character and start the game'
        Create_character_loop().cmdloop()

    def do_quit(self, arg):
        'Exit the game'
        return True


# Test class, will probably not be needed
class Create_character_loop(cmd.Cmd):
    intro = "Let's get you started!"
    prompt = "(Player): "

    def do_test(self, arg):
        print(arg)

    def do_quit(self, arg):
        Choose_class().cmdloop()
        return True


class Choose_class(cmd.Cmd):
    intro = "Choose what class you would like to play as"
    prompt = "(Player): "

    def do_ranger(self, arg):
        ('A ranger is quick on it\'s feet and relies mostly on dex\n'
         'ranger your_name')
        init_char(parse(arg))

    def do_mage(self, arg):
        'A mage cast spells to heal or deal damage, int is very important'
        pass

    def do_guardian(self, arg):
        'Chonky boi, takes hits, str and const'
        pass

    def do_cleric(self, arg):
        'Mix of mage and guardian, str and int'
        pass

    def do_quit(self, arg):
        return True



def init_char(name):
    os.chdir('./saves')
    try:
        with open(f"{name}.json", "x") as player:
            # json.dump(x, player)
            pass
    except FileExistsError:
        print("That character already exists")
    os.chdir('..')


def fix_input(arg):
    try:
        return int(arg)
    except ValueError:
        return arg.lower().strip()


def parse(arg):
    try:
        if "," in arg:
            return tuple(map(fix_input, arg.split(",")))
        else:
            return fix_input(arg)
    except Exception as e:
        print(f"Error: {e}")


Main_menue_loop().cmdloop()
