from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

sb_data = {}


@app.route('/score', methods=['GET', 'POST'])
def score():
    if request.method == 'POST':
        update = request.get_json()
        global sb_data
        sb_data[update['name']] = update['results']
    return jsonify(**sb_data)


if __name__ == '__main__':
    app.run(debug=True)
