from flask import Flask, render_template, request

import random

from scipy import rand

from service.wordSelector import wordSelector
from service.NumberGenerator import NumberGenerator

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello, World!"

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/name')
def number():
    name = 10
    return render_template('testDynamicNumber.html', name=name)

@app.route('/randomNumber', methods =["GET", "POST"])
def randomRN():
    if request.method == "POST":
        min = request.form.get("min")
        max = request.form.get("max")
        num = NumberGenerator.randomNumber(int(min),int(max))
        return render_template('randomNumberGenerator.html', number = str(num))
    return render_template('randomNumberGenerator.html')

@app.route('/randomWord', methods =["GET", "POST"])
def randomWS():
    inputString = None
    inputSeparator = None
    if request.method == "POST":
        inputString = request.form.get("inputString")
        inputSeparator = request.form.get("inputSeparator")
        WS = wordSelector.getWord(inputString, inputSeparator)
        return render_template('randomWordSelector.html', Rword = str(WS))
    return render_template('randomWordSelector.html')


if __name__ == '__main__':
    app.run(debug=True)