-- script that creates the table force_name on my MySQL server with name not null

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL);