from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')