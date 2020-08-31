

def check_input(input_options): # Seems to get angry, and make you write quit twice
    
        player_input = input(": ").lower() # Do fix
        
        if player_input == "help": # change to "!help(?)"
            
            print(input_options)
            return(False)
        else:

            if player_input in input_options:
                return(player_input)
            else: 
                print("Did you spell that right?\nTry again!\n"
                "To see your options again, type 'help'"
                )
                return(False) 