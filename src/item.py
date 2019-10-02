#item.py
class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

    def __repr__(self):
        return (f'item : {self.item_name}, description : {self.item_desc}')

    def on_take(self):
        print(f"You have picked up {self.item_name}")
    
    def on_drop(self):
        print(f"You have dropped {self.item_name}")


items = {
    'coins':  Item("coins",
                     "glittering gold coins"),

    'dagger':    Item("dagger", """a small sharp looking weapon. quite stabby"""),

    'emerald': Item("emerald", """a shiny green gemstone."""),

    'magic_hat':   Item("magic_hat", """a hat you can wear with 
    unkown consequences.  magical"""),

    'sneakers': Item("sneakers", """quiet shows for sneaking.  sneaky"""),

    'belt': Item("belt", """rope for holding up trousers""")
}