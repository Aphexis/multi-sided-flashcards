from flashcard import Set, Card
# from models import Set_SQL, Side_SQL, Card_SQL, Cell_SQL
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import insert
# import os
#
# from sqlalchemy import create_engine
# engine = create_engine('mysql://root:' + os.environ.get('password') + '@localhost/flashcards?auth_plugin=mysql_native_password')
# # Session = sessionmaker(bind=engine)
# # session = Session()
# conn = engine.connect()
from models import db, Set_SQL, Card_SQL, Side_SQL, Cell_SQL, User

### READ
def query_cells(card_id):  # returns a dictionary of cells {side_id: [info, card_id]} in the f for a given card_id
    records = db.session.query(Cell_SQL).filter_by(card_id=card_id).all()
    cells = {}
    for record in records:
        cells[record.side_id] = [record.info, record.card_id]
    return cells

def query_cards(id):  # returns an array of Card objects for a given set_id
    records = db.session.query(Card_SQL).filter_by(set_id=id).all()
    print("querying cards")
    print(records)
    cards = []
    for record in records:
        card = Card(record.card_ID, record.card_order, query_cells(record.card_ID), record.set_id)
        cards.append(card)
    return cards

# print(query_cards(25))

def query_sides(set_id):  # returns a dictionary of {id_name: [order, name, set_id]} for a given set_id
    records = db.session.query(Side_SQL).filter_by(set_id=set_id).all()
    sides = {}
    for record in records:
        sides[record.side_id] = [record.side_order, record.name, record.set_id]
    return sides

def query_sets():  # returns an array of all sets in [set_id, name, description]
    records = db.session.query(Set_SQL).all()
    sets = []
    for record in records:
        set = [record.set_id, record.name, record.description]
        sets.append(set)
    return sets

def build_sets():  # builds an array of Set objects for all sets in db using query methods
    records = query_sets()
    sets = []
    for record in records:
        set = Set(record[0], record[1], record[2], query_sides(record[0]), query_cards(record[0]))
        sets.append(set)
    return sets

def get_set(set_id):  # builds a Set object for a given set_id
    record = db.session.query(Set_SQL).filter_by(set_id=set_id).one()
    set = Set(record.set_id, record.name, record.description, query_sides(record.set_id), query_cards(record.set_id))
    return set


### WRITE
def process_form(form):
    # create set
    ins = Set_SQL(name=form['name'], description=form['description'])
    db.session.add(ins)
    db.session.commit()
    set_id = ins.set_id
    # ins = insert(Set_SQL).values(name=form['name'], description=form['description'])
    # set_result = conn.execute(ins)
    # set_id = set_result.inserted_primary_key[0]
    print(set_id)

    # create sides
    sides = []
    side_fields = dict(filter(lambda elem: 'cell[0]' in elem[0], form.items()))
    for field in side_fields:
        if field == 'cell[0][0]':
            ins_side = Side_SQL(set_id=set_id, name=form[field])
            db.session.add(ins_side)
            db.session.commit()
            side_id = ins_side.side_id
            # ins_side = insert(Side_SQL).values(set_id=set_id, name=form[field])
            # side_result = conn.execute(ins_side)
            # side_id = side_result.inserted_primary_key[0]
            print(side_id)
        else:
            side = {'set_id': set_id, 'name': form[field]}
            sides.append(side)
    if sides:
        side_result = db.engine.execute(Side_SQL.__table__.insert(), sides)

    # create cards
    cards = []
    card_fields = dict(filter(lambda elem: 'cell' in elem[0] and '][0]' in elem[0] and 'cell[0]' not in elem[0], form.items()))
    for field in card_fields:
        if field == 'cell[1][0]':
            ins_card = Card_SQL(set_id=set_id)
            db.session.add(ins_card)
            db.session.commit()
            card_id = ins_card.card_ID
            # ins_card = insert(Card_SQL).values(set_id=set_id)
            # card_result = conn.execute(ins_card)
            # card_id = card_result.inserted_primary_key[0]
            print(card_id)
        else:
            card = {'set_id': set_id}
            cards.append(card)
    if cards:
        card_result = db.engine.execute(Card_SQL.__table__.insert(), cards)

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
    cells_result = db.engine.execute(Cell_SQL.__table__.insert(), cells)

### DELETE
def delete_set(set_id):
    sides = query_sides(set_id)
    for side in sides:
        db.session.query(Cell_SQL).filter_by(side_id=side).delete()
    db.session.query(Side_SQL).filter_by(set_id=set_id).delete()
    db.session.query(Card_SQL).filter_by(set_id=set_id).delete()
    db.session.query(Set_SQL).filter_by(set_id=set_id).delete()
    db.session.commit()


