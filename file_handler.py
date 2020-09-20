import json
import character_creation as cc
import core_functionality as cf


# Serialization
def char_to_json(player):
    """
    Handler func for init_char which serializes character.
    This funcs object is to pick apart the player object,
    then turn it into a json
    """
    player_dict = {
        "name": player.name,
        "hp": player.hp,
        "defense": player.defense,
        "stats": {
                "dex": player.dex,
                "const": player.const,
                "str": player.str,
                "int": player.int
        },
        "pos": player.pos,
    }
    player_json = json.dumps(player_dict)
    return player_json

