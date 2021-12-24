-- script to create tables of states, city
-- using hbnb_dev_db database

USE hbnb_dev_db;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL PRIMARY KEY, name VARCHAR(60) NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME(0) NOT NULL);
CREATE TABLE IF NOT EXISTS cities (state_id INT NOT NULL FOREIGN KEY (states), name VARCHAR(128) NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL);
-- Adding values into states table
USE hbnb_dev_db;
INSERT INTO states (id, name, created_at, updated_at) VALUES (1, "California", CURDATE(), CURDATE());
INSERT INTO states (id, name, created_at, updated_at) VALUES (2, "Arizona", CURDATE(), CURDATE());
INSERT INTO states (id, name, created_at, updated_at) VALUES (3, "New York", CURDATE(), CURDATE());
INSERT INTO states (id, name, created_at, updated_at) VALUES (4, "Illinois", CURDATE(), CURDATE());
-- Adding values into cities table
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (1, "my_id_c", "San Francisco", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (2, "my_id_c", "San Jose", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (3, "my_id_c", "Los Angeles", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (4, "my_id_c", "Fremont", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (5, "my_id_c", "Palo Alto", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (6, "my_id_c", "Oakland", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (7, "my_id_a", "Page", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES (8, "my_id_a", "Phoenix", CURDATE(), CURDATE());

