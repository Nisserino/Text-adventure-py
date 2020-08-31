import core_functionality as cf
import dice

def create_character():

    def stat_choice(stats): 
        for x in range(4):
            
            if stats[x] == "int":
                player.int = dice_rolls[x]

            elif stats[x] == "dex":
                player.dex = dice_rolls[x]

            elif stats[x] == "str":
                player.str = dice_rolls[x]

            elif stats[x] == "const":
                player.const = dice_rolls[x]

    name = input("Hello, there!\nWhat are you called?: ").title()
    print(f"Greetings {name}!\nWhat is your profession?")   # add info when selecting something
    profession = input("(Ranger, Mage, Guardian, Cleric)\n: ").lower()

    if profession == "ranger":
        player = cf.Ranger(name)
    elif profession == "mage":
        player = cf.Mage(name)
    elif profession == "guardian":
        player = cf.Guardian(name)
    elif profession == "cleric":
        player = cf.Cleric(name)

    print(f"Hello {name} the {profession}\nLet's get you started!")

    dice_rolls = dice.stat_roller()

    #Maybe change the descriptions to a var, print var, and let player write !help to see description again.
    print(
        f"Your dice rolls are {dice_rolls}\nChoose where to put the first roll\n"
        "Int: Increases your intelligence, making you more proficient with spells!\n"
        "Dex: Increases your dexterity, making you more nimble and precise!\n"
        "Str: Increases your strength, making you stronger and making your hits heavier!\n"
        "Const: Increases your constitution, making you tougher and more durable!\n"
    )
    stat_1 = input("I want the first roll to go to: ").lower()
    stat_2 = input("I want the second roll to go to: ").lower()
    stat_3 = input("I want the third roll to go to: ").lower()
    stat_4 = input("I want the fourth roll to go to: ").lower()
    stats = []
    stats.extend((stat_1, stat_2, stat_3, stat_4))


    stat_choice(stats)
    return(player)
