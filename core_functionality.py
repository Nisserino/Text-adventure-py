"""
Contains character classes, Enemies, and methods of attack.

(Write more smart stuff, like how to call stuff)
"""
import dice
import inputs
class Player:
    """
    Parent class for the playable characters.

    To initialize a player, create an object from one of the children.
    When calling the Child class (eg. Ranger) call it with the characters name
    Example: player1 = Ranger("Pelle")
    """

    def __init__(self, name):
        self.name = name
        self.hp = 12
        self.defense = 10
        self.dex = 0
        self.const = 0
        self.str = 0
        self.int = 0
        self.init_roll = 0
        self.pos = [1, 1]

    def deal_dmg(self, roll, stat, target):

        if stat == "int":
            stat = self.int
        elif stat == "dex":
            stat = self.dex
        elif stat == "str":
            stat = self.str
        elif stat == "const":
            stat = self.const
        mod = (stat - 10) // 2
        dmg = roll + mod
        target.hp -= dmg
        print(f"You dealt {dmg}!")



class Ranger(Player):
    
    def __init__(self, name):
        Player.__init__(self, name)



    def stab(self, target):
        roll = dice.d4()
        crit = dice.d10()
        hit = dice.hit(self, self.dex)
        if crit == 10:
            roll += dice.d4() 
            print("Crit!")
        else:
            pass # pass or continue?
        
        if hit == True:
            self.deal_dmg(roll, self.dex, target)
        else:
            print("You swing, but you missed!\n")

        #fire 3 arrows at the same time!
        #Balance by decreasing hit chance for next arrow (first arrow is d20)
    def rapidhot_attack(self, target): # In future(when there are more enemies in combat)
                                        # change the attack to be able to attack more enemies

        for i in range(3):
            roll = dice.d4()
            hit = dice.hit(self, self.dex - i * 2) # test and balance
            if hit == True:
                dmg = roll
                self.deal_dmg(dmg, self.dex, target)
            else:
                print(f"{self.name} shot, but missed!")

        

    # add bool to see if attack is ranged or not
    # also add this to return value of function
    def shoot(self, target): 
        roll = dice.d6()

        hit =  dice.hit(self, self.dex)
        if hit == True:             
            self.deal_dmg(roll, self.dex, target)
        elif hit == False:
            print(f"{self.name} shot, but missed!\nOh the humility!\n")

        # Attacks
    def attack(self, target):
        options = ["dagger", "bow", "ability"]
        print(
            "What do you want to do?\n"
            "Use Dagger, Bow or Ability"
        )
        while True:
            choice = inputs.check_input(options)
            if choice != False:
                break
        
        if choice == "dagger":
            self.stab(target)

        elif choice == "bow":
            self.shoot(target)

        elif choice =="ability":
            options = ["rapidshot", "back"]
            print(
                "What ability do you want to use?\n"
                "'Rapidshot': Shoot the target 3 times\n"
                "'back': to go back to previous menue "
            )
            while True:
                ability = inputs.check_input(options)
                if ability != False:
                    break

            if ability == "rapidshot":
                self.rapidhot_attack(target)

            elif ability == "back":
                self.attack(target)

        

class Mage(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.mana = 15
        
    def spell_attack(self, user1, user2, spell_choice):
        try:
            dmg = user1.spells[spell_choice][0]
            user1.mana -= user1.spells[spell_choice][1]
            user2.hp -= dmg    
        except KeyError:
            print(f"Couldn't find spell '{spell_choice}'")
                
    spells = {
        "fireball": [7, 5],
        "frost bolt": [4, 3]
    }

class Guardian(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp = 20        

class Cleric(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.mana = 15



class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 12
        self.defense = 10
        self.dex = 0
        self.const = 0
        self.str = 0
        self.int = 0
        self.init_roll = 0

    def deal_dmg(self, roll, stat, target):

        if stat == "int":
            stat = self.int
        elif stat == "dex":
            stat = self.dex
        elif stat == "str":
            stat = self.str
        elif stat == "const":
            stat = self.const
        mod = (stat - 10) // 2
        dmg = roll + mod
        target.hp -= dmg
        print(f"{self.name} dealt {dmg} damage!")

class Skeleton(Enemy):
    def __init__(self):
        self.name = "Dooters"
        Enemy.__init__(self, self.name)
        self.blood = False
        self.curse_victim = []

    def scratch(self, target):
        roll = dice.d4()

        hit =  dice.hit(self, self.dex)
        if hit == True:
            self.deal_dmg(roll, self.dex, target)
            self.blood = True
        else:
            print("Couldn't break through defense!")
        
    def curse(self, target): # Change it into a while, that deals the player damage
                            # if curse == True on change to self.hp
        print("oooga boooga")

    def attack(self, target):

        if self.blood == False:
            self.scratch(target)
        elif self.blood == True:
            self.curse(target)

    



class Wolf(Enemy):
    def __init__(self):
        self.name = "Wolf"
        self.hp = 7

class Orc(Enemy):
    def __init__(self):
        self.name = "Orc"
        self.hp = 10



# player1 = Guardian("hello")
# print(player1.name)






#range_attack(p1, enemy1)
#spell_attack(p3, enemy1, input("Enter spell of choice: "))
#print(f'{p1.name} has {p1.arrows} arrows left \nwolf has {enemy1.hp} hp left')
#To set up basic run of game, lock in inf_loop, with input options
#move, look etc, before input, an if statement checks what is allowed to do.