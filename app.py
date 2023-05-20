from flask import Flask, render_template, request
from game_data import DATA
import os

app = Flask(__name__)

msg = [{'title': "message one"}]
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/template', methods=['GET'])
def template():
    return render_template('template.html')


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    print('values', request.values)
    return render_template('leaderboard.html', data=DATA)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
