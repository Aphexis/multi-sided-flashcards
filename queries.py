from flashcard import Set, Card
from models import Set_SQL, Side_SQL, Card_SQL, Cell_SQL
from sqlalchemy.orm import sessionmaker
# from app import engine

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:' + 'root!$23' + '@localhost/flashcards')
Session = sessionmaker(bind = engine)
session = Session()

# records = session.query(Side_SQL).filter_by(set_id=1).all()
# for record in records:
#     print(record.name)

### READ
def query_cells(card_id):  # returns a dictionary of cells {side_id: [info, card_id]} in the f for a given card_id
    records = session.query(Cell_SQL).filter_by(card_id=card_id).all()
    cells = {}
    for record in records:
        cells[record.side_id] = [record.info, record.card_id]
    return cells

# print(query_cells(1))


def query_cards(set_id):  # returns an array of Card objects for a given set_id
    records = session.query(Card_SQL).filter_by(set_id=set_id).all()
    cards = []
    for record in records:
        card = Card(record.card_ID, record.card_order, query_cells(record.card_ID), record.set_id)
        cards.append(card)
    return cards

# cards = query_cards(1)
# for card in cards:
#     print(card.id_num, card.cells)


def query_sides(set_id):  # returns a dictionary of {id_name: [order, name, set_id]} for a given set_id
    records = session.query(Side_SQL).filter_by(set_id=set_id).all()
    sides = {}
    for record in records:
        sides[record.side_id] = [record.side_order, record.name, record.set_id]
    return sides

# print(query_sides(1))


def query_sets():  # returns an array of all sets in [set_id, name, description]
    records = session.query(Set_SQL).all()
    sets = []
    for record in records:
        set = [record.set_id, record.name, record.description]
        sets.append(set)
    return sets

# print(query_sets())


def build_sets():  # builds an array of Set objects for all sets in db using query methods
    records = query_sets()
    sets = []
    for record in records:
        set = Set(record[0], record[1], record[2], query_sides(record[0]), query_cards(record[0]))
        sets.append(set)
    return sets

# sets = build_sets()
# for set in sets:
#     print(set.name, set.cards, set.description)


def get_set(set_id):  # builds a Set object for a given set_id
    record = session.query(Set_SQL).filter_by(set_id=set_id).one()
    set = Set(record.set_id, record.name, record.description, query_sides(record.set_id), query_cards(record.set_id))
    return set

# set = get_set(1)
# print(set.name, set.description, set.cards)
# print(set)
# cards = set.get_card_info()
# print(cards)

# card = query_cards(1)[0]
# print(card)
# print(card.get_info(query_sides(1)))
### WRITE
# create_set
# edit_set
