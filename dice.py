"""
Used to initialize characters and roll for their stats.
"""
import random
def stat_roller():

    def roll_dice():

        for _ in range(5):
            roll = random.randint(1, 6)
            rolls.append(roll)

    stats = []
    rolls = []
    
    for i in range(4):
        roll_dice()
        if i <= 1:
            rolls = sorted(rolls, reverse=True)
        else:
            rolls = sorted(rolls)
        to_stats = rolls[0:3]
        stats.append(to_stats[0] + to_stats[1] + to_stats[2])
    return(stats)
    

#d4, d6, d8, d10, d12, d20
def d4():
    return(random.randint(1,4))

def d6():
    return(random.randint(1,6))

def d8():
    return(random.randint(1,8))

def d10():
    return(random.randint(1,10))

def d12():
    return(random.randint(1,12))

def d20():
    return(random.randint(1,20))


    
def custom_dice(num_dice, range_min, range_max):

    for _ in range(num_dice):
        roll = random.randint(range_min, range_max)
        print(roll)


def hit(attacker, stat):

    roll = d20() # add crit option for d20 landing on 20
    
    if stat == "int":
        stat = attacker.int
    elif stat == "dex":
        stat = attacker.dex
    elif stat == "str":
        stat = attacker.str
    elif stat == "const":
        stat = attacker.const
    mod = (stat - 10) // 2
    
    if roll + mod >= 10:
        return True
    else:
        return False
