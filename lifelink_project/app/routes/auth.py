from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Donor, Taker
from app import db
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

# Donor Registration
@auth_bp.route('/register/donor', methods=['GET', 'POST'])
def register_donor():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        donor = Donor.query.filter_by(email=email).first()
        if donor:
            flash('Email already registered.')
            return redirect(url_for('auth.register_donor'))
        new_donor = Donor(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            address=request.form['address'],
            email=email,
            phone_no=request.form['phone_no'],
            date_of_birth=datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d'),
            blood_type=request.form['blood_type'],
            health_condition=request.form['health_condition']
        )
        new_donor.password_hash = generate_password_hash(password)
        db.session.add(new_donor)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login_donor'))
    return render_template('register_donor.html')

# Donor Login
@auth_bp.route('/login/donor', methods=['GET', 'POST'])
def login_donor():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        donor = Donor.query.filter_by(email=email).first()
        if donor and check_password_hash(getattr(donor, 'password_hash', ''), password):
            session['user_id'] = donor.donor_id
            session['user_type'] = 'donor'
            return redirect(url_for('dashboard.donor_dashboard'))
        flash('Invalid credentials.')
    return render_template('login_donor.html')

# Donor Dashboard
@auth_bp.route('/dashboard/donor')
def donor_dashboard():
    if session.get('user_type') != 'donor':
        return redirect(url_for('auth.login_donor'))
    donor = Donor.query.get(session['user_id'])
    return render_template('dashboard_donor.html', donor=donor)

# Taker Registration
@auth_bp.route('/register/taker', methods=['GET', 'POST'])
def register_taker():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        taker = Taker.query.filter_by(email=email).first()
        if taker:
            flash('Email already registered.')
            return redirect(url_for('auth.register_taker'))
        new_taker = Taker(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            address=request.form['address'],
            email=email,
            phone_no=request.form['phone_no'],
            date_of_birth=datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d'),
            blood_type=request.form['blood_type'],
            health_condition=request.form['health_condition']
        )
        new_taker.password_hash = generate_password_hash(password)
        db.session.add(new_taker)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login_taker'))
    return render_template('register_taker.html')

# Taker Login
@auth_bp.route('/login/taker', methods=['GET', 'POST'])
def login_taker():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        taker = Taker.query.filter_by(email=email).first()
        if taker and check_password_hash(getattr(taker, 'password_hash', ''), password):
            session['user_id'] = taker.taker_id
            session['user_type'] = 'taker'
            return redirect(url_for('dashboard.taker_dashboard'))
        flash('Invalid credentials.')
    return render_template('login_taker.html')

# Taker Dashboard
@auth_bp.route('/dashboard/taker')
def taker_dashboard():
    if session.get('user_type') != 'taker':
        return redirect(url_for('auth.login_taker'))
    taker = Taker.query.get(session['user_id'])
    return render_template('dashboard_taker.html', taker=taker)

# Logout
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index')) 