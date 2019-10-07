class Set:
    def __init__ (self, id_num, name, description, sides, cards):
        self.id_num = id_num
        self.name = name
        self.description = description
        self.sides = sides
        self.cards = cards
    
    def num_cards(self):
        return len(self.cards)
    
    def num_sides(self):
        return len(self.sides)
    
    def get_side_names(self):
        side_names = ['#']
        for i in range(len(self.sides)):
            side_names.append(self.sides[i][1])
        return side_names