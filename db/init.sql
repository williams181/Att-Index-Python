create database myflask;
use myflask;

CREATE TABLE funcionario (
  nome VARCHAR(50),
  email VARCHAR(50)
);

INSERT INTO funcionario
  (nome, email)
VALUES
  ('william', 'william@gmail.com'),
  ('vagner', 'vagner@hotmail.com');