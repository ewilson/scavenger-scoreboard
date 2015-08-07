from flask import Flask, request, jsonify, render_template
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)


@app.route('/')
def index():
    return render_template('index.html')

sb_data = {'sb': []}


#
# To Post a score send {"pid": 0, "results": [ ... ]}
#
@app.route('/score', methods=['GET', 'POST'])
def score():
    if request.method == 'POST':
        update = request.get_json()
        global sb_data
        players = sb_data['sb']
        for i, player in enumerate(players):
            if player['pid'] == update['pid']:
                players[i]['results'] = update['results']
    return jsonify(**sb_data)


#
# To Post a new player, send {"player_name": "My Name"}
#
@app.route('/player', methods=['POST'])
def player():
    data = request.get_json()
    global sb_data
    players = sb_data['sb']
    pid = len(players)
    new_player = {'pid': pid, 'player_name': data['player_name'], 'results': [0]*15}
    players.append(new_player)
    return jsonify(**new_player)

if __name__ == '__main__':
    app.run(debug=True)
