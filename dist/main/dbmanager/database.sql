CREATE TABLE user(username TEXT, password TEXT, secret_phrase TEXT);
CREATE TABLE passwords(pid TEXT, password TEXT, site TEXT, created TEXT, username vachar(255) null);
CREATE TABLE controller(registered VARCHAR(1) NOT NULL);
INSERT INTO controller (registered) VALUES ('0');

-- Impano Manzi enock