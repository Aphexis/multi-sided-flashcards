class Set:
    def __init__ (self, id_num, name, sides, cards):
        self.id_num = id_num
        self.name = name
        self.sides = sides
        self.cards = cards
    
    def num_cards(self):
        return len(self.cards)
    
    def num_sides(self):
        return len(self.sides)