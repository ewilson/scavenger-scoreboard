from flask import Flask, request, jsonify, render_template
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)


@app.route('/')
def index():
    return render_template('index.html')

sb_data = {'sb': [
    {'pid': 1, 'player_name': 'Dalton & Riley',
     'results': [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
    {'pid': 2, 'player_name': 'Grant & Daniel',
     'results': [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0]}
    ]}


@app.route('/score', methods=['GET', 'POST'])
def score():
    if request.method == 'POST':
        update = request.get_json()
        global sb_data
        sb_data[update['name']] = update['results']
    return jsonify(**sb_data)


if __name__ == '__main__':
    app.run(debug=True)
