# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, player_room):
        self.player_name = player_name
        self.player_room = player_room
        self.player_items = []

    def __repr__(self):
        return (f'name:{self.player_name}, room:{self.player_room.room_name}, items:{self.player_items}')
