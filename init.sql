-- Active: 1701801198772@@127.0.0.1@3306@fruiticart
USE fruiticart;

DROP TABLE IF EXISTS fidelity;
DROP TABLE IF EXISTS `client`;
DROP TABLE IF EXISTS `order`;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS fruit;
DROP TABLE IF EXISTS vegetable;
DROP TABLE IF EXISTS order_detail;
DROP TABLE IF EXISTS warehouse;
DROP TABLE IF EXISTS stock;

-- create tables
CREATE TABLE IF NOT EXISTS fidelity (
    `type` ENUM('Gold','Silver','Without') NOT NULL PRIMARY KEY,
    discount DECIMAL(5,2)
);

CREATE TABLE IF NOT EXISTS `client` (
    mail VARCHAR(50) NOT NULL PRIMARY KEY,
    `password` VARCHAR(50),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    phone_number VARCHAR(10),
    `address` VARCHAR(50),
    postal_code VARCHAR(5),
    credit_card VARCHAR(16),
    `type` ENUM('Gold','Silver','Without') NOT NULL
);

CREATE TABLE IF NOT EXISTS `order` (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    delivery_date DATE,
    delivery_address VARCHAR(50),
    delivery_postal_code VARCHAR(5),
    `status` ENUM('Pending','Confirmed','In transit','Delivered','Cancelled'),
    total_price DECIMAL(10,2),
    mail VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS fruit (
    fruit_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30),
    price DECIMAL(5,2),
    origin VARCHAR(30),
    product_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS vegetable (
    vegetable_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30),
    price DECIMAL(5,2),
    origin VARCHAR(30),
    product_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS order_detail (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT
);

CREATE TABLE IF NOT EXISTS warehouse (
    warehouse_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `address` VARCHAR(50),
    postal_code VARCHAR(5),
    `zone` ENUM('North','South','East','West')
);

CREATE TABLE IF NOT EXISTS stock (
    warehouse_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT
);

-- add primary keys
ALTER TABLE order_detail ADD CONSTRAINT pk_order_detail PRIMARY KEY (order_id, product_id);
ALTER TABLE stock ADD CONSTRAINT pk_stock PRIMARY KEY (warehouse_id, product_id);

-- add foreign keys
ALTER TABLE `client` ADD CONSTRAINT fk_client_fidelity FOREIGN KEY (`type`) REFERENCES fidelity(`type`);
ALTER TABLE `order` ADD CONSTRAINT fk_order_mail FOREIGN KEY (mail) REFERENCES `client`(mail);
ALTER TABLE fruit ADD CONSTRAINT fk_fruit_product_id FOREIGN KEY (product_id) REFERENCES product(product_id);
ALTER TABLE vegetable ADD CONSTRAINT fk_vegetable_product_id FOREIGN KEY (product_id) REFERENCES product(product_id);
ALTER TABLE order_detail ADD CONSTRAINT fk_order_detail_order_id FOREIGN KEY (order_id) REFERENCES `order`(order_id);
ALTER TABLE order_detail ADD CONSTRAINT fk_order_detail_product_id FOREIGN KEY (product_id) REFERENCES product(product_id);
ALTER TABLE stock ADD CONSTRAINT fk_stock_warehouse_id FOREIGN KEY (warehouse_id) REFERENCES warehouse(warehouse_id);
ALTER TABLE stock ADD CONSTRAINT fk_stock_product_id FOREIGN KEY (product_id) REFERENCES product(product_id);