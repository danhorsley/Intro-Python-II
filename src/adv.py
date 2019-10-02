from room import Room
from player import Player
from item import *
import random

# Declare all the rooms
# minor change
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#randomly assign items to room
for key in room:
    items_in_room = random.choice(list(range(1,4)))
    for i in range(items_in_room):
        if i == 0 :
            pass
        else:
            item_select = random.choice(list(items.keys()))
            room[key].room_items.append(items[item_select])



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("creating new player")
p1 = Player("player 1",room['outside'])
print(p1)
print(p1.player_room)
my_input = []
my_input.append('place holder')
while my_input[0] != 'q':
    try:
        my_input = input('please input your command oh master :   ')
        my_input = my_input.split(' ')
        if my_input[0] in ['n','N',"North","north"]:
            p1.player_room = p1.player_room.n_to
        if my_input[0] in ['s','S',"South","south"]:
            p1.player_room = p1.player_room.s_to
        if my_input[0] in ['e','E',"East","east"]:
            p1.player_room = p1.player_room.e_to
        if my_input[0] in ['w','W',"West","west"]:
            p1.player_room = p1.player_room.w_to
        if my_input[0] in ['pick up','get',"take","acquire"]:
            p1.player_items.append(items[my_input[1]])
            p1.player_room.room_items.remove(items[my_input[1]])
            items[my_input[1]].on_take()
        if my_input[0] in ['drop','ditch',"lose","punt"]:
            p1.player_items.remove(items[my_input[1]])
            p1.player_room.room_items.append(items[my_input[1]])
            items[my_input[1]].on_drop()
        if my_input[0] in ['i','inv',"inventory","stuff"]:
            print('in your inventory you hold a ')
            for i in p1.player_items:
                print(i.item_name)
        if my_input[0] in ['look','search',"observe"]:
            print('in the room you see a ')
            for j in p1.player_room.room_items:
                print(j.item_name)
        print(p1)
        print(p1.player_room)
    except:
        print("you can't go that way!!!")
