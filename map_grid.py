import inputs
import core_functionality as cf
player = cf.Ranger
player.pos = [1, 2]

# mirrored coordinate systemed (horrible, how fix)
map_grid = [        # map size 10x10
    [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],
    [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],
    [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],
    [[4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10]],
    [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],
    [[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10]],
    [[7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10]],
    [[8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10]],
    [[9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10]],
    [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]]
]
map_size_x = 10
map_size_y = 10


def moving(player):
    special_move_options = []  # add list of special options, such as in a town etc
    
    def check_options(player_position, *special_option):
        # check where player can move
        # Fix something for special options (Where it is handled)

        check_x = [False, False]  # left, right
        if player_position[0] - 1 >= 1:
            check_x[0] = True
        if player_position[0] + 1 <= map_size_x:
            check_x[1] = True

        check_y = [False, False]  # up, down
        if player_position[1] - 1 >= 1:
            check_y[0] = True
        if player_position[1] + 1 <= map_size_x:
            check_y[1] = True
        return(check_x + check_y)

    def move():
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
            player.pos[0] -= 1
            print("Moved west")

        elif choice == "east":
            player.pos[0] += 1
            print("Moved east")

        elif choice == "north":
            player.pos[1] -= 1
            print("Moved north")

        elif choice == "south":
            player.pos[1] += 1
            print("Moved south")

    move()


for i in range(9):
    moving(player)
