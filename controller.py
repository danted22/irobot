from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_name(username=None):
    if request.method == 'POST':
        return render_template("controller.html", action=request.form['button'])
    else:
        return render_template("controller.html", action=None)
