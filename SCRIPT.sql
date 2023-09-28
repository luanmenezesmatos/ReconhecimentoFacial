/* Criando o script de criação do banco de dados e suas respectivas tabelas. */

-- Criando o banco de dados
CREATE DATABASE IF NOT EXISTS `db_recfacial`;

-- Selecionando o banco de dados
USE `db_recfacial`;

-- Criando a tabela `faces`
CREATE TABLE IF NOT EXISTS `faces` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `image` BLOB NULL,
  PRIMARY KEY (`id`)
);

SHOW TABLES;

SELECT * FROM faces;

SELECT image FROM faces WHERE name = "LuanMenezes";