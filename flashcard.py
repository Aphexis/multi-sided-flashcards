class Set:
    def __init__ (self, id_num, name, description, sides, cards):
        # add side_names and card_info as properties?
        self.id_num = id_num
        self.name = name
        self.description = description
        self.sides = sides  # array of Side objects
        self.cards = cards  # array of Card objects
    
    def num_cards(self):
        return len(self.cards)

    def num_sides(self):
        return len(self.sides)

    def get_side_names(self):  # unordered
        side_names = ['#']
        for i in range(len(self.sides)):
            side_names.append(self.sides.get_name)
        return side_names

    def get_card_info(self):  # unordered
        cards_info = []
        for i in range(len(self.cards)):
            card_info = [i, self.cards[i].get_info]  # can you do it all in one statement?
            cards_info.append(card_info)
        return cards_info  # 2D array of card info

    def reorder(self): # do we need this?
        # reorders the cards based on card order?
        return


class Side:  # CHANGE INTO A DICTIONARY: {id_name: [order, name, set_id]}
    def __init__ (self, id_num, order, name, set_id):
        self.id_num = id_num
        self.order = order
        self.name = name
        self.set_id = set_id  # the set that the side belongs to (?)

    def get_name(self):
        return self.name

    def get_order(self):
        return self.order

    # do something with the order?


class Card:
    def __init__ (self, id_num, order, cells, set_id):
        self.id_num = id_num
        self.order = order
        self.cells = cells  # array of Cell objects
        self.set_id = set_id  # the set that the card belongs to (?)

    def get_info_dict(self):
        return  # dictionary of {side_name: side_info}

    def get_info(self):
        # returns an array of the card's info in the order of the sides
        # using info from side order and the dictionary of cells
        return  # kajdlaskjd

    def get_order(self):
        return self.order

class Cell:  # CHANGE INTO A DICTIONARY of {side_id: info, card_id}
    def __init__ (self, info, metadata, side_id, card_id):
        self.info = info
        self.side_id = side_id
        self.card_id = card_id

    def get_info(self):
        return self.info

    def get_side_id(self):
        return self.side_id