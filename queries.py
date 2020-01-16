from flashcard import Set, Card
from models import Set_SQL, Side_SQL, Card_SQL, Cell_SQL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
import os

from sqlalchemy import create_engine
engine = create_engine('mysql://root:' + os.environ.get('password') + '@localhost/flashcards?auth_plugin=mysql_native_password')
# Session = sessionmaker(bind=engine)
# session = Session()
conn = engine.connect()


### READ
def query_cells(card_id, session):  # returns a dictionary of cells {side_id: [info, card_id]} in the f for a given card_id
    records = session.query(Cell_SQL).filter_by(card_id=card_id).all()
    cells = {}
    for record in records:
        cells[record.side_id] = [record.info, record.card_id]
    return cells

def query_cards(id, session):  # returns an array of Card objects for a given set_id
    records = session.query(Card_SQL).filter_by(set_id=id).all()
    print("querying cards")
    print(records)
    cards = []
    for record in records:
        card = Card(record.card_ID, record.card_order, query_cells(record.card_ID, session), record.set_id)
        cards.append(card)
    return cards

# print(query_cards(25))

def query_sides(set_id, session):  # returns a dictionary of {id_name: [order, name, set_id]} for a given set_id
    records = session.query(Side_SQL).filter_by(set_id=set_id).all()
    sides = {}
    for record in records:
        sides[record.side_id] = [record.side_order, record.name, record.set_id]
    return sides

def query_sets(session):  # returns an array of all sets in [set_id, name, description]
    records = session.query(Set_SQL).all()
    sets = []
    for record in records:
        set = [record.set_id, record.name, record.description]
        sets.append(set)
    return sets

def build_sets(session):  # builds an array of Set objects for all sets in db using query methods
    records = query_sets(session)
    sets = []
    for record in records:
        set = Set(record[0], record[1], record[2], query_sides(record[0], session), query_cards(record[0], session))
        sets.append(set)
    return sets

def get_set(set_id, session):  # builds a Set object for a given set_id
    record = session.query(Set_SQL).filter_by(set_id=set_id).one()
    set = Set(record.set_id, record.name, record.description, query_sides(record.set_id, session), query_cards(record.set_id, session))
    return set


### WRITE
def process_form(form):
    # create set
    ins = insert(Set_SQL).values(name=form['name'], description=form['description'])
    set_result = conn.execute(ins)
    set_id = set_result.inserted_primary_key[0]
    print(set_id)

    # create sides
    sides = []
    side_fields = dict(filter(lambda elem: 'cell[0]' in elem[0], form.items()))
    for field in side_fields:
        if field == 'cell[0][0]':
            ins_side = insert(Side_SQL).values(set_id=set_id, name=form[field])
            side_result = conn.execute(ins_side)
            side_id = side_result.inserted_primary_key[0]
            print(side_id)
        else:
            side = {'set_id': set_id, 'name': form[field]}
            sides.append(side)
    if sides:
        side_result = conn.execute(insert(Side_SQL), sides)

    # create cards
    cards = []
    card_fields = dict(filter(lambda elem: 'cell' in elem[0] and '][0]' in elem[0] and 'cell[0]' not in elem[0], form.items()))
    for field in card_fields:
        if field == 'cell[1][0]':
            ins_card = insert(Card_SQL).values(set_id=set_id)
            card_result = conn.execute(ins_card)
            card_id = card_result.inserted_primary_key[0]
            print(card_id)
        else:
            card = {'set_id': set_id}
            cards.append(card)
    if cards:
        card_result = conn.execute(insert(Card_SQL), cards)

    # create cells
    cells = []
    cell_fields = dict(filter(lambda elem: 'cell' in elem[0] and 'cell[0]' not in elem[0], form.items()))
    # records = session.query(Card_SQL.card_ID).filter_by(set_id=id).all()
    # print(records)
    for field in cell_fields:
        card_index = int(field[5:6])-1
        side_index = int(field[-2:-1])
        print(card_index)
        print(side_index)
        cell = {'card_id': card_index+card_id, 'side_id': side_id+side_index, 'info': form[field]}
        cells.append(cell)
    cells_result = conn.execute(insert(Cell_SQL), cells)


