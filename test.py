# def combat(player, enemy):
#     first = combat_start(player, enemy)
#     if first == "player":
#         player.turn = "first"
#         enemy.turn = "second"

#     elif first == "enemy":
#         enemy.turn = "first"
#         player.turn = "second"

#     #start combat
#     while player.hp >= 0 and enemy.hp >= 0: # Why doesn't combat die?
#         #Start fighting
#         if player.turn == "first":
#             order = [player, enemy]
#         elif enemy.turn == "first":
#             order = [enemy, player]

#         order[0].attack(order[1])
#         print(f"{order[1].name} has {order[1].hp} hp left!")
#         order[1].attack(order[0])
#         print(f"{order[0].name} has {order[0].hp} hp left!\n")
#     print("fight done")  

# just in case


def crypt(text):
    changed = []
    for char in text:
        changed.append(ord(char))
    salted = []

    print(changed)
    i = 0
    for _ in changed:
        if i % 2 == 0:
            salted.append(changed[i]+3)
        elif i in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
            salted.append(changed[i]-7)
        else:
            salted.append(changed[i])     

        i += 1
    return(changed)

def de_crypt(crypt_list):
    to_chr = []

    i = 0
    for _ in crypt_list:
        
        if i % 2 == 0:
            to_chr.append(crypt_list[i]-3)
        elif i in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
            to_chr.append(crypt_list[i]+7)
        
        else:
            to_chr.append(crypt_list[i])
        i += 1
    print(to_chr)
    for char in to_chr:
        print(chr(char))

text = "Kryptera mig!"

crypt_list = crypt(text)
de_crypt(crypt_list)