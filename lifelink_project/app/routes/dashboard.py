from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Donor, Taker, Offer, Request as RequestModel, Donation

dash_bp = Blueprint('dashboard', __name__)

@dash_bp.route('/dashboard/donor')
def donor_dashboard():
    if session.get('user_type') != 'donor':
        return redirect(url_for('auth.login_donor'))
    donor = Donor.query.get(session['user_id'])
    offers = Offer.query.filter_by(donor_id=donor.donor_id).all()
    donations = Donation.query.filter_by(donor_id=donor.donor_id).all()
    return render_template('dashboard_donor.html', donor=donor, offers=offers, donations=donations)

@dash_bp.route('/dashboard/taker')
def taker_dashboard():
    if session.get('user_type') != 'taker':
        return redirect(url_for('auth.login_taker'))
    taker = Taker.query.get(session['user_id'])
    requests = RequestModel.query.filter_by(taker_id=taker.taker_id).all()
    donations = Donation.query.filter_by(taker_id=taker.taker_id).all()
    return render_template('dashboard_taker.html', taker=taker, requests=requests, donations=donations) 