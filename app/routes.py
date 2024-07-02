from flask import (flash, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_jwt_extended import create_access_token

from app import app, db
from app.models import User


@app.route('/')
def home():
    return send_from_directory('templates', 'home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return send_from_directory('templates', 'login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {}!'.format(username), 'success')
        return redirect(url_for('login'))
    return send_from_directory('templates', 'register.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Tajmahal.html')
def taj_mahal():
    return render_template('Tajmahal.html')

@app.route('/Petra.html')
def petra():
    return render_template('Petra.html')

@app.route('/China.html')
def great_wall_of_china():
    return render_template('China.html')

@app.route('/christ_the_redeemer.html')
def christ_the_redeemer():
    return render_template('christ_the_redeemer.html')

@app.route('/Colosseum.html')
def colosseum():
    return render_template('Colosseum.html')

@app.route('/Chichen_itza.html')
def chichen_itza():
    return render_template('Chichen_itza.html')

@app.route('/Machu_picchu.html')
def machu_picchu():
    return render_template('Machu_picchu.html')