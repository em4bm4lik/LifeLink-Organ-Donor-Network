DROP DATABASE IF EXISTS lifelink;
CREATE DATABASE lifelink;
USE lifelink;

CREATE TABLE Hospital (
    hospital_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    email VARCHAR(100),
    phone_no VARCHAR(20)
);

CREATE TABLE Organ (
    organ_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50),
    `condition` VARCHAR(100),
    expiry DATE,
    hospital_id INT,
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);

CREATE TABLE Donor (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(255),
    email VARCHAR(100),
    phone_no VARCHAR(20),
    date_of_birth DATE,
    blood_type VARCHAR(5),
    health_condition TEXT,
    password_hash VARCHAR(255)
);

CREATE TABLE Taker (
    taker_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(255),
    email VARCHAR(100),
    phone_no VARCHAR(20),
    date_of_birth DATE,
    blood_type VARCHAR(5),
    health_condition TEXT,
    password_hash VARCHAR(255)
);

CREATE TABLE Offer (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    organ_type VARCHAR(50),
    status VARCHAR(50),
    donor_id INT,
    organ_id INT,
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (organ_id) REFERENCES Organ(organ_id)
);

CREATE TABLE Request (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    organ_type VARCHAR(50),
    urgency VARCHAR(50),
    status VARCHAR(50),
    taker_id INT,
    FOREIGN KEY (taker_id) REFERENCES Taker(taker_id)
);

CREATE TABLE Donation (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    status VARCHAR(50),
    donor_id INT,
    taker_id INT,
    organ_id INT,
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (taker_id) REFERENCES Taker(taker_id),
    FOREIGN KEY (organ_id) REFERENCES Organ(organ_id)
);
