from typing import List

from flask import Flask, g, render_template, request

from models.player import Player
from models.table import BlackjackTable

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "BAD_SECRET_KEY"


# @app.route('/_test_ajax')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)


# @app.route('/test_ajax')
# def test_ajax_index():
#     return render_template('test_ajax.html')


@app.route('/basic_strategy/')
def basic_strategy_index():
    """Page explaining basic strategy"""
    pass


single_player_table = None


@app.route('/basic_strategy/playing', methods=['GET', 'POST'])
def basic_strategy_playing():
    """Playing basic strategy"""
    global single_player_table
    if not single_player_table:
        single_player_table = _create_single_player_table()

    if request.method == 'POST':
        if request.form.get("hand_index"):
            hand_index = int(request.form.get("hand_index")) - 1

            if "hit" in request.form:
                print("hitting...")
                print(f"hand_index:{hand_index}")
                single_player_table.player.hit(
                    single_player_table.shoe.pop(), hand_index)

        if "deal" in request.form:
            single_player_table.deal_everyone()

        if "reset" in request.form:
            single_player_table.reset()

    return render_template('playing_basic_strategy.html', table=single_player_table)


def _create_single_player_table(n_decks: int = 1):
    print("No table existing in g, creating a new one...")
    table = BlackjackTable(n_decks=n_decks)
    table.add_player(Player("Anon", br_balance=1000))
    return table
