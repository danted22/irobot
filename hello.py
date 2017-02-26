from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
def hello_name(username=None):
    return render_template("hello.html", name=username)
