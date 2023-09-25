/* Criando o script de criação do banco de dados e suas respectivas tabelas. */

-- Criando o banco de dados
CREATE DATABASE IF NOT EXISTS `db_recfacial`;

-- Selecionando o banco de dados
USE `db_recfacial`;

-- Criando a tabela `faces`
CREATE TABLE IF NOT EXISTS `faces` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `image` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
);