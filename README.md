# A textbased, dnd-esq adventuregame made in python

## Terminal based single player
Would be really nice to make it into a multiplayer game, but that's gonna be a while untill that will be realistic.

### In development

- A map, so that you can actually move around
- A start, and end to combat (interactions in generall)
- An inventory system (json?)
- 1 - 2 attacks (min) for each player/enemy
- Enemy attack choice system
- Making sure units can't deal negative damage
- Skellys special stats, and how curse should be implemented
- Menue interaction (including a help command, and text for it)
- check_input needs a fix (if wrong input, or help you need to give the actual argument twice for it to work)
- check_input might be put in another file aswell (broader subject: structure functions to files is what's goin' on.)

### For tomorow (or just later) me!


3. Try to move a player object around the "map"
4. Make map bigger(if 3 works)
5. Give "back" statement in the input for move options if someone doesn't wanna go anywhere
6. Refactor and rename move() in map_grid

### Bigger shite to figure out

- A saving system of any kind, otherwise, program wipes out after exiting.
- Story-line

- Failsafe, so that you're not thrown out with a type error if you write something wrong.
- Failsafe for when an attack roll would make you deal a negative number in damage(abs would make -1 = 1, so find something else)
- Game progression, one idea is to create a start quest for each class, and have that as the game tutorial. After completion you get to play with other people, and have a background based on your choices in the tutorial
- Implement space in combat, and make range a thing worth wile

### For later

1. More classes
2. More enemies
3. More attacks
4. Crits if d20 lands on 20
5. Add level for player, and scale enemies with it(or initialize level when creating enemy obj, randomize enemy levels
6. (also add exp)
7. Make the text prettier on character creation

### Stats 

1. constitution = life
2. dexterity = precision
3. strength = raw attack damage
4. intelligence = mana and magic damage
5. defense = armour for the hit rolls, base: 10 on players
6. hp = raw hp, modified by constitution

>Stat to add later (Add descriptors)
1. Wisdom : modifyer on some magic attacks/utility spells
    Also modifyer for spell slots
2. Perception : Modifyer for hit rate
3. Charisma(?) : Modifyer for dialog options, increases chance to convice others
4. Speed : How fast you can move through the battleground, could also be initiative modifyer 

### Stat roller

In character_creation.py
Wrap everything in a function to call from \_\_main__ when game is run?

## Weapons

>Dagger
Low base damage, 1/10 chance to crit

>Bow
Mid base damage, ranged weapon

## Abilities

### Enemy abilities

#### Skeleton
>Scratch
Use to extract blood from players and deal som damage.
prerequisite for curse ability

>Curse
Ability to curse a player when it get's ahold of their blood

When curse is activated the skeleton is bound to that player, so that when the skeleton takes damage, the player does so aswell

Skeleton can also break it's own bones to hurt the bound player.


- Counter: holy damage, deals low damage and removes curse
Put that shit on cleric

### Player abilities

#### Ranger
>Dagger

>Multishot
Fire 3 arrows at the same time
d4 damage rolls for each arrow
Roll for hit on each arrow
Hitchance decreased for each hit

>Bow

## Doing now

# Combat

>Trying to figure out how to implement
Take player and enemy

roll d20 + dex modifier ((dex-10)//2)
to roll for initiative

Lock player with enemy in combat using while loop

>How combat works

- action face
choose action (attack, more?)
when attacking, roll to see if you break through enemy defense
roll d20
roll >= enemy.defense = hit

Is there a stat mod to modify hit chance?
(It's in the code, but should it be there?)

if hit, roll for damage
roll x dxx dice to see how much damage you do.

check line 27, core_functionality

