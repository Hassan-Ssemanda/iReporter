from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesytem'
Session(app)

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/')
def recordCreate():
    return render_template('recordCreate.html')

@app.route('/intervation')
def intervation():
    return render_template('intervation.html')

@app.route('/profile/<username>')
def profile():
    return render_template('profile.html')

@app.route('/admin', methods = [])
def admin():
    return render_template('admin.html')