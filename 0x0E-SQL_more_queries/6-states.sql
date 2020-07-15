-- script that creates the database hbtn_0d_usa and the table states in it on my MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256)
);