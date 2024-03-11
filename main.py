from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello There"


@app.route('/fruit')
def sweet_fruit():
    fruit = ["apple", "bannana", "pineapple", "orange"]
    return random.choice(fruit)

@app.route('/number')
def lucky_number():
    return str(random.randint(0,100))
