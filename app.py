from typing import List

from flask import Flask, redirect, render_template, url_for

from models.table import BlackjackTable
from models.player import Player

app = Flask(__name__)
app.config.from_object('config')

TABLES = [
    BlackjackTable(id=1),
    BlackjackTable(id=2),
]


def get_table(table_id: int, tables: List[BlackjackTable]):
    for table in tables:
        if table.id == table_id:
            return table


@app.route('/')
def hello():
    return 'Hello World!'


# @app.route('/table/')
# @app.route('/table/<table_id>')
# def table(table_id: int = None):
#     print(table_id)
#     if table_id:
#         table = get_table(table_id, TABLES)
#         if table:
#             return render_template('table_id.html', table=table)
#         # return redirect(url_for('table'))
#     return render_template('table.html')


@app.route('/basic_strategy/')
def basic_strategy_index():
    """Page explaining basic strategy"""
    pass

@app.route('/basic_strategy/playing')
def basic_strategy_playing():
    """Playing basic strategy"""
    table = BlackjackTable(n_decks=1)
    player = Player("Anon", br_balance=1000)
    table.add_player(player)
    player.hit(table.shoe.pop())
    player.hit(table.shoe.pop())
    return render_template('playing_basic_strategy.html', table=table, player=player)
