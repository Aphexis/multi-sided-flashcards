# Class and object representations for flashcard sets and cards

class Set:
    def __init__ (self, id_num, name, description, sides, cards, user, public):
        self.id_num = id_num
        self.name = name
        self.description = description
        self.sides = sides  # array of Side dictionaries
        self.cards = cards  # array of Card objects
        self.user = user  # user who owns the set
        self.public = public  # if True, any user can view these sets
    
    def num_cards(self):
        return len(self.cards)

    def num_sides(self):
        return len(self.sides)

    def get_side_names(self):
        side_names = ['#']
        for id_num in self.sides:
            side_names.append(self.sides[id_num][1])
        return side_names

    def get_card_info(self):
        cards_info = []
        for i in range(len(self.cards)):
            card_info = [i+1] + self.cards[i].get_info(self.sides)
            cards_info.append(card_info)
        return cards_info  # 2D array of card info

#Side: dictionary of {id_num: [order, name, set_id]}

class Card:
    def __init__ (self, id_num, order, cells, set_id):
        self.id_num = id_num
        self.order = order
        self.cells = cells  # array of Cell objects
        self.set_id = set_id  # the set that the card belongs to

    def get_info(self, sides):  # returns an array of the card's cell info in the order of the sides
        info = []
        for side in sides:
            cell_info = self.cells.get(side)
            if cell_info is not None:
                info.append(cell_info[0])
        return info

    def get_order(self):
        return self.order

# Cell: dictionary of {side_id: info, card_id}