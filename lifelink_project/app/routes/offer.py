from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import Offer, Organ, Donor
from app import db
from datetime import datetime

offer_bp = Blueprint('offer', __name__)

@offer_bp.route('/offers')
def list_offers():
    offers = Offer.query.all()
    return render_template('offers.html', offers=offers)

@offer_bp.route('/offer/add', methods=['GET', 'POST'])
def add_offer():
    if session.get('user_type') != 'donor':
        flash('Only donors can add offers.')
        return redirect(url_for('auth.login_donor'))
    organs = Organ.query.all()
    if request.method == 'POST':
        offer = Offer(
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            organ_type=request.form['organ_type'],
            status=request.form['status'],
            donor_id=session['user_id'],
            organ_id=request.form['organ_id']
        )
        db.session.add(offer)
        db.session.commit()
        flash('Offer added!')
        return redirect(url_for('offer.list_offers'))
    return render_template('offer_form.html', organs=organs)

@offer_bp.route('/offer/edit/<int:offer_id>', methods=['GET', 'POST'])
def edit_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    if session.get('user_type') != 'donor' or offer.donor_id != session.get('user_id'):
        flash('You can only edit your own offers.')
        return redirect(url_for('offer.list_offers'))
    organs = Organ.query.all()
    if request.method == 'POST':
        offer.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        offer.organ_type = request.form['organ_type']
        offer.status = request.form['status']
        offer.organ_id = request.form['organ_id']
        db.session.commit()
        flash('Offer updated!')
        return redirect(url_for('offer.list_offers'))
    return render_template('offer_form.html', offer=offer, organs=organs)

@offer_bp.route('/offer/delete/<int:offer_id>')
def delete_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    if session.get('user_type') != 'donor' or offer.donor_id != session.get('user_id'):
        flash('You can only delete your own offers.')
        return redirect(url_for('offer.list_offers'))
    db.session.delete(offer)
    db.session.commit()
    flash('Offer deleted!')
    return redirect(url_for('offer.list_offers')) 