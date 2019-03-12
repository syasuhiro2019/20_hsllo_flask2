import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return render_template('index.html', message='Hi Hachimantai!')


@app.route('/dice', methods=['GET'])
def dice():
    result = random.randint(1, 6)

    return render_template('dice.html', result=result)


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return render_template('user_name.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
