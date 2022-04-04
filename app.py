from flask import Flask, render_template, request

import random

from scipy import rand
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
def randomAB():
    if request.method == "POST":
        min = request.form.get("min")
        max = request.form.get("max")
        num = random.randint(int(min), int(max))
        return render_template('randomNumberGenerator.html', number = str(num))
    return render_template('randomNumberGenerator.html')


if __name__ == '__main__':
    app.run(debug=True)