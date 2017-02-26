from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the main page. Try putting your name in after the slash.'

@app.route('/<username>')
def hello_name(username):
    return "Hello {}!".format(username)
