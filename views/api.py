from flask import Blueprint, render_template, request, url_for
api_blueprint = Blueprint('api', __name__, template_folder='templates')
from sqlalchemy.orm import sessionmaker
from queries import get_set, engine, delete_set

@api_blueprint.route('/', methods=['GET'])
def set():
    set_id = request.args.get('set_id')
    side_num = int(request.args.get('side_num'))
    card_num = int(request.args.get('card_num'))
    Session = sessionmaker(bind=engine)
    session = Session()
    set = get_set(set_id, session)
    # set_info = set.get_card_info()
    sides = set.get_side_names()
    cards = set.get_card_info()
    curr_side = sides[side_num]
    next_side = sides[side_num+1] if side_num+1 < len(sides) else None
    card_info = cards[card_num][side_num]
    # print(set_info)
    # return "you clicked set #" + str(set_id)
    return render_template('study-card.html', curr_side=curr_side, next_side=next_side, card_info=card_info)