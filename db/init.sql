create database myflask;
use myflask;

CREATE TABLE funcionario (
  id int NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50),
  email VARCHAR(50),
  PRIMARY KEY (id)
);

INSERT INTO funcionario
  (nome, email)
VALUES
  ('william', 'william@gmail.com'),
  ('vagner', 'vagner@hotmail.com');