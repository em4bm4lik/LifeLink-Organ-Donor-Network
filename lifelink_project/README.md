# LifeLink: Organ Donation Management System

A web-based platform that is designed to connect organ donors, recipients, and hospitals to streamline the donation process.

## What is LifeLink?

LifeLink makes organ donation easier by bringing donors, recipients, and hospitals together on one platform. You can register as a donor or recipient, browse available organs from hospitals, make donation offers or requests, and get matched with compatible candidates.

## Key Features

- Register as a donor or organ recipient
- Browse hospitals and their available organs
- Create and track donation offers and requests
- Get matched with compatible donors/recipients
- View your donation history and status updates
- Manage health profiles with blood type and conditions

## Prerequisites

You will need:
- Python 3.7+
- MySQL Server
- pip (comes with Python)

## Quick Start

### 1. Set up your environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate              # Windows
# source venv/bin/activate         # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure the database

Open `setup_db.py` and update your MySQL credentials:

```python
user='YOUR_DB_USERNAME_HERE_(Usually "root")',  # Replace this
password='YOUR_DB_PASSWORD_HERE'                 # Replace this
```

Then open `config.py` and update the database URI with the same credentials:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{YOUR_DB_USERNAME_HERE_(Usually_[root])}:{YOUR_DB_PASSWORD_HERE}@localhost/lifelink'
```

### 3. Initialize and run

```bash
# Create the database and tables
python setup_db.py

# Start the application
python run.py
```

That's it! The app will open at http://127.0.0.1:5000

## Troubleshooting

**Database connection error?**
- Make sure MySQL is running
- Double-check your username and password in both files
- Confirm the database name stays as `lifelink`

**Port 5000 already in use?**
- Edit `run.py` and change `app.run(debug=True)` to `app.run(debug=True, port=5001)`

**Import errors?**
- Make sure your virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
