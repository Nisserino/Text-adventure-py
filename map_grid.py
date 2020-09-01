import inputs
import core_functionality as cf
player = cf.Ranger
player.pos = [1,2]

#mirrored coordinate systemed (horrible, how fix)
map_grid = [        # map size 2x2 
    [[1, 1],[1, 2]],
    [[2, 1],[2, 2]]
]
map_size_x = 2
map_size_y = 2

def move(player):
    special_move_options = [] # add list of special options, such as in a town etc
    

    def check_options(player_position, *special_option):
        #check where player can move
        # Fix something for special options (Where it is handled)

        check_x = [False, False] # left, right
        if player_position[0] - 1 >= 1:
            check_x[0] = True
        if player_position[0] + 1 <= map_size_x:
            check_x[1] = True

        check_y = [False, False] # up, down
        if player_position[1] - 1 >= 1:
            check_y[0] = True
        if player_position[1] + 1 <= map_size_x:
            check_y[1] = True

        
        return(check_x + check_y)

    move_options = check_options(player.pos)
    base_options = ["West", "East", "North", "South"]
    options = []
    index = 0
    for option in move_options:
        if option == True:
            options.append(base_options[index].lower())
        else:
            pass
        index += 1
    
    print(f"Your options are: {options}")

    while True:
        choice = inputs.check_input(options)
        if choice != False:
            break

    if choice == "west":
        print("shite")
        
    elif choice == "east":
        print("True shite")
        
    elif choice == "north":
        print("Norrut")
        
    elif choice == "south":
        pass
        

move(player)