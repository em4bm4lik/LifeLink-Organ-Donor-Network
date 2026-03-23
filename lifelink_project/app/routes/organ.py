from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Organ, Hospital
from app import db
from datetime import datetime

organ_bp = Blueprint('organ', __name__)

@organ_bp.route('/organs')
def list_organs():
    organs = Organ.query.all()
    return render_template('organs.html', organs=organs)

@organ_bp.route('/organ/add', methods=['GET', 'POST'])
def add_organ():
    hospitals = Hospital.query.all()
    if request.method == 'POST':
        organ = Organ(
            type=request.form['type'],
            condition=request.form['condition'],
            expiry=datetime.strptime(request.form['expiry'], '%Y-%m-%d'),
            hospital_id=request.form['hospital_id']
        )
        db.session.add(organ)
        db.session.commit()
        flash('Organ added!')
        return redirect(url_for('organ.list_organs'))
    return render_template('organ_form.html', hospitals=hospitals)

@organ_bp.route('/organ/edit/<int:organ_id>', methods=['GET', 'POST'])
def edit_organ(organ_id):
    organ = Organ.query.get_or_404(organ_id)
    hospitals = Hospital.query.all()
    if request.method == 'POST':
        organ.type = request.form['type']
        organ.condition = request.form['condition']
        organ.expiry = datetime.strptime(request.form['expiry'], '%Y-%m-%d')
        organ.hospital_id = request.form['hospital_id']
        db.session.commit()
        flash('Organ updated!')
        return redirect(url_for('organ.list_organs'))
    return render_template('organ_form.html', organ=organ, hospitals=hospitals)

@organ_bp.route('/organ/delete/<int:organ_id>')
def delete_organ(organ_id):
    organ = Organ.query.get_or_404(organ_id)
    db.session.delete(organ)
    db.session.commit()
    flash('Organ deleted!')
    return redirect(url_for('organ.list_organs')) 