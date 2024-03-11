from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello There"


@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return str(int(num1)+int(num2))
    
@app.route('/sub/<num1>/<num2>')
def sub(num1, num2):
    return str(int(num1)-int(num2))
    
@app.route('/multi/<num1>/<num2>')
def multi(num1, num2):
    return str(int(num1)*int(num2))
    
@app.route('/div/<num1>/<num2>')
def div(num1, num2):
    return str(int(num1)/int(num2))
