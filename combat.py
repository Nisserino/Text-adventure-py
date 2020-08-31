import dice
import core_functionality as cf

player = cf.Ranger("pelle")
player.dex = 12 
enemy = cf.Skeleton()
enemy.dex = 8
enemy2 = cf.Skeleton()
enemy2.dex = 7

def init_roll(roll):
    return(roll.init_roll)

def combat(player, *enemy):

    all_units = combat_start(player, *enemy)
    enemy_list = all_units[1:]
    all_units.sort(reverse=True,key=init_roll)

    for i in all_units:
        print(i.name, i.init_roll)
    #start combat
    while player.hp > 0 and enemy_list[0].hp > 0: 
        #Start fighting
        for unit in all_units:
            if isinstance(unit, cf.Player):
                print("Who do you want to attack")
                enemy_num = 0
                for i in enemy_list:
                    print(f"{i.name}, {i.hp}, to target: '{enemy_num}'")
                    enemy_num += 1
                attack = int(input(": "))

                unit.attack(enemy_list[attack])

                if enemy_list[attack].hp <= 0 and len(enemy_list) > 1:
                    del enemy_list[attack]
                elif player.hp <= 0:
                    print("You died")
                    break
                else:
                    pass
            else: 
                if unit.hp > 0:
                    unit.attack(player)
                else:
                    pass

    print("fight done")        


#bow attack usage
# print(enemy.hp)
# player.attack(enemy)
# print(enemy.hp)


def combat_start(player, *enemy):
    units = []

    player_d20 = dice.d20()
    player_mod = (player.dex - 10) // 2
    player_roll = player_d20 + player_mod
    player.init_roll = player_roll # change to initiative_roll
    print(f"Player: {player_d20}, modified to {player_roll}")
    units.append(player)
    
    for unit in enemy:
        
        enemy_d20 = dice.d20()
        enemy_mod = (unit.dex - 10) // 2
        enemy_roll = enemy_d20 + enemy_mod
        unit.init_roll = enemy_roll
        print(f"Enemy: {enemy_roll}")
        units.append(unit)

  
    print(f"Player roll: {player_d20}\nEnemy roll: {enemy_roll}")
    
    return(units)

combat(player, enemy, enemy2)
