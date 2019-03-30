from flask import Flask, render_template, Response, request, redirect, url_for, make_response

app = Flask(__name__)

def setCamera(cam):
    global camera
    camera = cam
    print(camera)

def setContourProcessor(contourProc):
    global contourProcessor
    contourProcessor = contourProc

@app.route('/')
def index():
    if ('H_MIN') in request.cookies:
        h_min = request.cookies.get('H_MIN')
        h_max = request.cookies.get('H_MAX')
        s_min = request.cookies.get('S_MIN')
        s_max = request.cookies.get('S_MAX')
        v_min = request.cookies.get('V_MIN')
        v_max = request.cookies.get('V_MAX')

    return render_template('index.html')

# Get data from HSV sliders
@app.route('/', methods=['POST'])
def HSV_post():
    h_min = request.form['H_MIN']
    h_max = request.form['H_MAX']
    s_min = request.form['S_MIN']
    s_max = request.form['S_MAX']
    v_min = request.form['V_MIN']
    v_max = request.form['V_MAX']
    
    # Write HSV values to file to preserve after reboot
    with open('values.txt', 'w') as f:
        f.write(h_min + "\n" + 
                s_min + "\n" + 
                v_min + "\n" +
                h_max + "\n" +
                s_max + "\n" +
                v_max + "\n")

    # Have the contour processor update its HSV bounds
    if contourProcessor:
        contourProcessor.getHSVBounds()

    # Redirect to video stream
    resp = make_response(render_template('index.html'))
    resp.set_cookie('H_MIN', h_min)
    resp.set_cookie('H_MAX', h_max)
    resp.set_cookie('S_MIN', s_min)
    resp.set_cookie('S_MAX', s_max)
    resp.set_cookie('V_MIN', v_min)
    resp.set_cookie('V_MAX', v_max)

    return resp


def gen():
    while True:
        frame = camera.getMJPEGProcessedFrame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def run():
    app.run(host='localhost', debug=False)
