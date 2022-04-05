from flask import Flask, render_template, request

import random

from scipy import rand

from service.wordSelector import wordSelector
from service.numberGenerator import NumberGenerator
from service.ranPWordGenerator import ranPWordGenerator
from service.randomSequenceGenerator import randomSequenceGenerator
from service.randomCardPick import randomCardPick

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello, World!"

@app.route('/index')
def index1():
    return render_template('index.html')

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

@app.route('/index/<length>/<type>')
def randomPassword(length, type):
    return ranPWordGenerator(int(length),str(type)).generate()

@app.route('/indeS/<length>')
def randomSeqGene(length):
    return randomSequenceGenerator(int(length)).generate()

@app.route('/card')
def randomCardGene():
    return randomCardPick().pick()

@app.route('/card/<num>')
def randomMCardGene(num):
    return randomCardPick().pickNum(int(num))


if __name__ == '__main__':
    app.run(debug=True)