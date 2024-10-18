create database blood;
use blood;


-- Create table to store donor details 
CREATE TABLE donor_details (
    donor_id INT AUTO_INCREMENT NOT NULL,
    donor_name VARCHAR(50) NOT NULL,
    donor_number VARCHAR(10) NOT NULL,
    donor_mail VARCHAR(50),
    donor_age INT NOT NULL,
    donor_gender VARCHAR(10) NOT NULL,
    donor_blood VARCHAR(10) NOT NULL,
    donor_address VARCHAR(100) NOT NULL,
    PRIMARY KEY (donor_id)
);


--  Create table for admin information 
CREATE TABLE admin_info (
    admin_id INT AUTO_INCREMENT NOT NULL,
    admin_name VARCHAR(50) NOT NULL,
    admin_username VARCHAR(50) NOT NULL UNIQUE,
    admin_password VARCHAR(100) NOT NULL,  -- Increased password length for security
    PRIMARY KEY (admin_id)
);

/* Insert sample admin data into admin_info */
INSERT INTO admin_info (admin_name, admin_username, admin_password)
VALUES ("Varun", "varunsardana004", 'password_hash');  -- Use hashed passwords for security

/* Create table to store blood groups */
CREATE TABLE blood (
    blood_id INT AUTO_INCREMENT NOT NULL,
    blood_group VARCHAR(10) NOT NULL,
    PRIMARY KEY (blood_id)
);

/* Insert blood group data */
INSERT INTO blood (blood_group)
VALUES ("B+"), ("B-"), ("A+"), ("O+"), ("O-"), ("A-"), ("AB+"), ("AB-");

/* Create table to store static pages (if needed) */
CREATE TABLE pages (
    page_id INT AUTO_INCREMENT NOT NULL,
    page_name VARCHAR(255) NOT NULL,
    page_type VARCHAR(50) UNIQUE NOT NULL,
    page_data LONGTEXT NOT NULL,
    PRIMARY KEY (page_id)
);

/* Optional: Insert sample static page data (for web content management) */
INSERT INTO pages (page_name, page_type, page_data) 
VALUES 
('Why Become Donor ?? ', 'donor', 'Some information about why to donate blood...its good'),
('About Us :', 'blood bank savings lifes ', 'Add New Mumbai ');

/* Create table to store contact information for the blood bank */
CREATE TABLE contact_info (
    contact_id INT AUTO_INCREMENT NOT NULL,
    contact_address VARCHAR(100) NOT NULL,
    contact_mail VARCHAR(50) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    PRIMARY KEY (contact_id)
);

/* Insert sample contact information */
INSERT INTO contact_info (contact_address, contact_mail, contact_phone)
VALUES ("Hisar, Haryana (125001)", "bloodbank@gmail.com", "7056550477");

/* Create table to store user contact queries */
CREATE TABLE contact_query (
    query_id INT AUTO_INCREMENT NOT NULL,
    query_name VARCHAR(100) NOT NULL,
    query_mail VARCHAR(120) NOT NULL,
    query_number CHAR(10) NOT NULL,
    query_message LONGTEXT NOT NULL,
    query_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    query_status INT DEFAULT 2,  -- 2 represents "Pending"
    PRIMARY KEY (query_id)
);

/* Insert a sample query */
INSERT INTO contact_query (query_name, query_mail, query_number, query_message)
VALUES ("Anuj", "anuj@gmail.com", "9923471025", "I need O+ blood.");

/* Update the query status */
UPDATE contact_query SET query_status = 1 WHERE query_id = 1;  -- 1 represents "Read"

/* Create table for query status types */
CREATE TABLE query_stat (
    id INT NOT NULL UNIQUE,
    query_type VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);

/* Insert status types */
INSERT INTO query_stat (id, query_type)
VALUES (1, "Read"), (2, "Pending");  create a stream lit application for this 