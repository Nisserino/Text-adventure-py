def check_input(input_options):

    player_input = input(": ").lower()

    if player_input == "help":

        print(input_options)
        return(False)
    else:

        if player_input in input_options:
            return(player_input)
        else:
            print(
                "Did you spell that right?\nTry again!\n"
                "To see your options again, type 'help'"
                )
            return(False)
