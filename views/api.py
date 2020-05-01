from flask import Blueprint, render_template, request, json
api_blueprint = Blueprint('api', __name__, template_folder='templates')
from sqlalchemy.orm import sessionmaker
from queries import get_set, engine

@api_blueprint.route('/card', methods=['GET'])
def card():
    # add authentication later so you can only access these routes if the user can view this set
    set_id = request.args.get('set')
    side_num = int(request.args.get('side')) # side number, where the first side is #1
    card_num = int(request.args.get('card')) # card number, where the first card is #0

    Session = sessionmaker(bind=engine)
    session = Session()
    set = get_set(set_id, session)
    session.close()

    sides = set.get_side_names()
    cards = set.get_card_info()
    curr_side = sides[side_num]
    next_side = sides[side_num+1] if side_num+1 < len(sides) else sides[1]
    card_info = cards[card_num][side_num]
    total_sides = len(sides) - 1

    return render_template('study-card.html', side_num=side_num, total_sides=total_sides, curr_side=curr_side, next_side=next_side, card_info=card_info)


@api_blueprint.route('/set_info', methods=['GET'])
def info():
    set_id = request.args.get('set')
    Session = sessionmaker(bind=engine)
    session = Session()
    set = get_set(set_id, session)
    num_cards = set.num_cards()
    num_sides = set.num_sides()
    sides = set.get_side_names()
    cards = set.get_card_info()
    session.close()
    return json.jsonify({
        'num_cards': num_cards,
        'num_sides': num_sides,
        'sides': sides,
        'cards': cards,
    })


@api_blueprint.route('/study_done', methods=['GET'])
def done():
    set_id = request.args.get('set')
    Session = sessionmaker(bind=engine)
    session = Session()
    set = get_set(set_id, session)
    num_cards = set.num_cards()
    session.close()
    return render_template('study-done.html', set_id=set_id, num_cards=num_cards)
