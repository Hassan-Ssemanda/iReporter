from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geolocation_flag')
def geolocation_flag():
    return render_template('geolocation_flag.html')

@app.route('/image_flag')
def image_flag():
    return render_template('image_flag.html')

@app.route('/video_flag')
def video_flag():
    return render_template('video_flag.html')

@app.route('/intervation')
def intervation():
    return render_template('intervation.html')

@app.route('/intervation_geolocation')
def intervation_geolocation():
    return render_template('intervation_geolocation.html')

@app.route('/intervation_image')
def intervation_image():
    return render_template('intervation_image.html')

@app.route('/intervation_video')
def intervation_video():
    return render_template('intervation_video.html')

@app.route('/recordCreate')
def recordCreate():
    return render_template('recordCreate.html')
