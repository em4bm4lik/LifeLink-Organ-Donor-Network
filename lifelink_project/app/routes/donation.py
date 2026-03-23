from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import Donation, Donor, Taker, Organ, Offer, Request as RequestModel
from app import db
from datetime import datetime

donation_bp = Blueprint('donation', __name__)

@donation_bp.route('/donations')
def list_donations():
    donations = Donation.query.all()
    return render_template('donations.html', donations=donations)

@donation_bp.route('/donation/add', methods=['GET', 'POST'])
def add_donation():
    donors = Donor.query.all()
    takers = Taker.query.all()
    organs = Organ.query.all()
    if request.method == 'POST':
        donation = Donation(
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            status=request.form['status'],
            donor_id=request.form['donor_id'],
            taker_id=request.form['taker_id'],
            organ_id=request.form['organ_id']
        )
        db.session.add(donation)
        db.session.commit()
        flash('Donation added!')
        return redirect(url_for('donation.list_donations'))
    return render_template('donation_form.html', donors=donors, takers=takers, organs=organs)

@donation_bp.route('/donation/edit/<int:donation_id>', methods=['GET', 'POST'])
def edit_donation(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    donors = Donor.query.all()
    takers = Taker.query.all()
    organs = Organ.query.all()
    if request.method == 'POST':
        donation.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        donation.status = request.form['status']
        donation.donor_id = request.form['donor_id']
        donation.taker_id = request.form['taker_id']
        donation.organ_id = request.form['organ_id']
        db.session.commit()
        flash('Donation updated!')
        return redirect(url_for('donation.list_donations'))
    return render_template('donation_form.html', donation=donation, donors=donors, takers=takers, organs=organs)

@donation_bp.route('/donation/delete/<int:donation_id>')
def delete_donation(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    db.session.delete(donation)
    db.session.commit()
    flash('Donation deleted!')
    return redirect(url_for('donation.list_donations'))

# Simple matching page to create a donation from offer/request
@donation_bp.route('/match', methods=['GET', 'POST'])
def match():
    offers = Offer.query.filter_by(status='Available').all()
    requests = RequestModel.query.filter_by(status='Pending').all()
    if request.method == 'POST':
        offer_id = int(request.form['offer_id'])
        request_id = int(request.form['request_id'])
        offer = Offer.query.get(offer_id)
        req = RequestModel.query.get(request_id)
        if offer and req and offer.organ_type == req.organ_type:
            donation = Donation(
                date=datetime.now(),
                status='Completed',
                donor_id=offer.donor_id,
                taker_id=req.taker_id,
                organ_id=offer.organ_id
            )
            offer.status = 'Matched'
            req.status = 'Matched'
            db.session.add(donation)
            db.session.commit()
            flash('Donation created from match!')
            return redirect(url_for('donation.list_donations'))
        else:
            flash('Organ type must match!')
    return render_template('match.html', offers=offers, requests=requests) 