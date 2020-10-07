from flask import Blueprint, render_template, request, json
api_blueprint = Blueprint('api', __name__, template_folder='templates')
from queries import get_set

@api_blueprint.route('/set_info', methods=['GET'])
def info():
    set_id = request.args.get('set')
    set = get_set(set_id)
    num_cards = set.num_cards()
    num_sides = set.num_sides()
    sides = set.get_side_names()
    cards = set.get_card_info()
    return json.jsonify({
        'num_cards': num_cards,
        'num_sides': num_sides,
        'sides': sides,
        'cards': cards,
    })


@api_blueprint.route('/study_done', methods=['GET'])
def done():
    set_id = request.args.get('set')
    set = get_set(set_id)
    num_cards = set.num_cards()
    return render_template('study-done.html', set_id=set_id, num_cards=num_cards)
