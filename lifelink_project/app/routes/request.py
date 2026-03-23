from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import Request as RequestModel, Taker
from app import db
from datetime import datetime

request_bp = Blueprint('request', __name__)

@request_bp.route('/requests')
def list_requests():
    requests = RequestModel.query.all()
    return render_template('requests.html', requests=requests)

@request_bp.route('/request/add', methods=['GET', 'POST'])
def add_request():
    if session.get('user_type') != 'taker':
        flash('Only takers can add requests.')
        return redirect(url_for('auth.login_taker'))
    if request.method == 'POST':
        req = RequestModel(
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            organ_type=request.form['organ_type'],
            urgency=request.form['urgency'],
            status=request.form['status'],
            taker_id=session['user_id']
        )
        db.session.add(req)
        db.session.commit()
        flash('Request added!')
        return redirect(url_for('request.list_requests'))
    return render_template('request_form.html')

@request_bp.route('/request/edit/<int:request_id>', methods=['GET', 'POST'])
def edit_request(request_id):
    req = RequestModel.query.get_or_404(request_id)
    if session.get('user_type') != 'taker' or req.taker_id != session.get('user_id'):
        flash('You can only edit your own requests.')
        return redirect(url_for('request.list_requests'))
    if request.method == 'POST':
        req.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        req.organ_type = request.form['organ_type']
        req.urgency = request.form['urgency']
        req.status = request.form['status']
        db.session.commit()
        flash('Request updated!')
        return redirect(url_for('request.list_requests'))
    return render_template('request_form.html', req=req)

@request_bp.route('/request/delete/<int:request_id>')
def delete_request(request_id):
    req = RequestModel.query.get_or_404(request_id)
    if session.get('user_type') != 'taker' or req.taker_id != session.get('user_id'):
        flash('You can only delete your own requests.')
        return redirect(url_for('request.list_requests'))
    db.session.delete(req)
    db.session.commit()
    flash('Request deleted!')
    return redirect(url_for('request.list_requests')) 