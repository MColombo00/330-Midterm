from flask import Flask, render_template #import flask and render template
app = Flask(__name__)

@app.route('/')#using the default route to render the startMenu html file
def greeting():
    return render_template('startMenu.html')


@app.route('/add/<num1>/<num2>') #uses the /add route to add two numbers
def add(num1, num2):
    return str(int(num1)+int(num2))#converts strings to integers and adds
    
@app.route('/sub/<num1>/<num2>') #uses the /sub route to subtract two  numbers
def sub(num1, num2):
    return str(int(num1)-int(num2))
    
@app.route('/multi/<num1>/<num2>') #uses the /multi route to multiply two  numbers
def multi(num1, num2):
    return str(int(num1)*int(num2))
    
@app.route('/div/<num1>/<num2>') #uses the /div route to divide two numbers
def div(num1, num2):
    return str(int(num1)/int(num2))
