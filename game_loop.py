import character_creation as cc
import inputs
"""
Will handle the basic loop of the game
Contains the basic menue
Is the games run-file
"""
def start_game():
    """
    Function to start the game
    """
    main_menue()

def check_input(input_options): # Seems to get angry, and make you write quit twice
    
    player_input = input(": ").lower() # Do fix
    
    if player_input == "help": # change to "!help(?)"
        
        print(input_options)
        check_input(input_options)
    else:

        if player_input in input_options:
            return(player_input)
        else: 
            print("Did you spell that right?\nTry again!\n"
            "To see your options again, type 'help'"
            )
            check_input(input_options) 


def check_saves():
    #initialize base_loop with player object
    pass

def main_menue():
    print(
        "Welcome to the game!\n"
        "What would you like to do?\n"
        "'Saves': to check for saved characters\n"
        "'Start': to initialize a new character\n"
        "'Quit': To exit the game"
        )
    options = ["saves", "start", "quit"]

    while True:
        choice = check_input(options)
        if choice != False:
            break
    
    if choice == "saves":
        pass
    elif choice == "start":
        base_loop()
    elif choice == "quit":
        exit
    else:
        print("Did you spell that right?\nTry again!\n"
            "To see your options again, type 'options'"
        )
        choice = inputs.check_input(options)    
    

def options(): # Will probably not be needed?
    """
    Options:

    !save : Saves the game
    !quit : Quits the game without saving
    !sq : Saves and quits the game
    Back : Goes back to previous menue
    """
    pass

def base_loop(*save):
    """
    Basic menue run loop
    Actions:
    !help : Prints out all your current options
    north, south, west, east
    talk
    Options : See options (Save, quit and help)
    """
    if save:
        # something like player = player.json
        pass
    else:
        print("Let's get you started!")
        player = cc.create_character()
    
    while True:
        pass

    
main_menue()
