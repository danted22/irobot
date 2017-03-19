import robo_api as ra
from camera import Camera
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_name(username=None):
    """Main controlling page."""
    if request.method == 'POST':
        return render_template("controller.html", action=ra.Test(request.form['button']))
    else:
        return render_template("controller.html", action=None)

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')