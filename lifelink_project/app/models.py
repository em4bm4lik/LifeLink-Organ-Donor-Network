from . import db

class Hospital(db.Model):
    __tablename__ = 'hospital'
    hospital_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    email = db.Column(db.String(100))
    phone_no = db.Column(db.String(20))
    organs = db.relationship('Organ', backref='hospital', lazy=True)

class Organ(db.Model):
    __tablename__ = 'organ'
    organ_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    condition = db.Column(db.String(100))
    expiry = db.Column(db.Date)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    offers = db.relationship('Offer', backref='organ', lazy=True)
    donations = db.relationship('Donation', backref='organ', lazy=True)

class Donor(db.Model):
    __tablename__ = 'donor'
    donor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(255))
    email = db.Column(db.String(100), unique=True)
    phone_no = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    blood_type = db.Column(db.String(5))
    health_condition = db.Column(db.Text)
    password_hash = db.Column(db.String(255))
    offers = db.relationship('Offer', backref='donor', lazy=True)
    donations = db.relationship('Donation', backref='donor', lazy=True)

class Taker(db.Model):
    __tablename__ = 'taker'
    taker_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(255))
    email = db.Column(db.String(100), unique=True)
    phone_no = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    blood_type = db.Column(db.String(5))
    health_condition = db.Column(db.Text)
    password_hash = db.Column(db.String(255))
    requests = db.relationship('Request', backref='taker', lazy=True)
    donations = db.relationship('Donation', backref='taker', lazy=True)

class Offer(db.Model):
    __tablename__ = 'offer'
    offer_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    organ_type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.donor_id'))
    organ_id = db.Column(db.Integer, db.ForeignKey('organ.organ_id'))

class Request(db.Model):
    __tablename__ = 'request'
    request_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    organ_type = db.Column(db.String(50))
    urgency = db.Column(db.String(50))
    status = db.Column(db.String(50))
    taker_id = db.Column(db.Integer, db.ForeignKey('taker.taker_id'))

class Donation(db.Model):
    __tablename__ = 'donation'
    donation_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    status = db.Column(db.String(50))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.donor_id'))
    taker_id = db.Column(db.Integer, db.ForeignKey('taker.taker_id'))
    organ_id = db.Column(db.Integer, db.ForeignKey('organ.organ_id')) 