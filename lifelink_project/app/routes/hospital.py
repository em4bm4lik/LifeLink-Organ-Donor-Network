from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Hospital
from app import db

hospital_bp = Blueprint('hospital', __name__)

@hospital_bp.route('/hospitals')
def list_hospitals():
    hospitals = Hospital.query.all()
    return render_template('hospitals.html', hospitals=hospitals)

@hospital_bp.route('/hospital/add', methods=['GET', 'POST'])
def add_hospital():
    if request.method == 'POST':
        hospital = Hospital(
            name=request.form['name'],
            address=request.form['address'],
            email=request.form['email'],
            phone_no=request.form['phone_no']
        )
        db.session.add(hospital)
        db.session.commit()
        flash('Hospital added!')
        return redirect(url_for('hospital.list_hospitals'))
    return render_template('hospital_form.html')

@hospital_bp.route('/hospital/edit/<int:hospital_id>', methods=['GET', 'POST'])
def edit_hospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    if request.method == 'POST':
        hospital.name = request.form['name']
        hospital.address = request.form['address']
        hospital.email = request.form['email']
        hospital.phone_no = request.form['phone_no']
        db.session.commit()
        flash('Hospital updated!')
        return redirect(url_for('hospital.list_hospitals'))
    return render_template('hospital_form.html', hospital=hospital)

@hospital_bp.route('/hospital/delete/<int:hospital_id>')
def delete_hospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    db.session.delete(hospital)
    db.session.commit()
    flash('Hospital deleted!')
    return redirect(url_for('hospital.list_hospitals')) 