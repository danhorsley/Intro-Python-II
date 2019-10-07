# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.room_items = []

    def __repr__(self):
        return (f'''Room : {self.room_name}, description : {self.description},
                    items : {self.room_items}''')