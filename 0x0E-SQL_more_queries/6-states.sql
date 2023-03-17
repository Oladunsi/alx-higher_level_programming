-- creates the database hbtn_0d_usa and the table states 
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- set db to hbtn_0d_usa
-- USE `hbtn_0d_usa`;
-- creates table states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`
    (`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
    `name` VARCHAR(256) NOT NULL, PRIMARY KEY(`id`));
