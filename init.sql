-- Active: 1701801198772@@127.0.0.1@3306@fruiticart
USE fruiticart;

DROP TABLE IF EXISTS order_fidelity;
DROP TABLE IF EXISTS `order_client`;
DROP TABLE IF EXISTS `order_order`;
DROP TABLE IF EXISTS order_product;
DROP TABLE IF EXISTS order_fruit;
DROP TABLE IF EXISTS order_vegetable;
DROP TABLE IF EXISTS order_orderdetail;
DROP TABLE IF EXISTS order_warehouse;
DROP TABLE IF EXISTS order_stock;

-- create tables
CREATE TABLE IF NOT EXISTS order_fidelity (
    `type` ENUM('Gold','Silver','Without') NOT NULL PRIMARY KEY,
    discount DECIMAL(5,2)
);

CREATE TABLE IF NOT EXISTS `order_client` (
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

CREATE TABLE IF NOT EXISTS `order_order` (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    delivery_date DATE,
    delivery_address VARCHAR(50),
    delivery_postal_code VARCHAR(5),
    `status` ENUM('Pending','Confirmed','In transit','Delivered','Cancelled'),
    total_price DECIMAL(10,2),
    mail VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS order_product (
    product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS order_fruit (
    fruit_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30),
    price DECIMAL(5,2),
    origin VARCHAR(30),
    product_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS order_vegetable (
    vegetable_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30),
    price DECIMAL(5,2),
    origin VARCHAR(30),
    product_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS order_orderdetail (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT
);

CREATE TABLE IF NOT EXISTS order_warehouse (
    warehouse_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `address` VARCHAR(50),
    postal_code VARCHAR(5),
    `zone` ENUM('North','South','East','West')
);

CREATE TABLE IF NOT EXISTS order_stock (
    warehouse_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT
);

-- add primary keys
ALTER TABLE order_orderdetail ADD CONSTRAINT pk_order_detail PRIMARY KEY (order_id, product_id);
ALTER TABLE order_stock ADD CONSTRAINT pk_stock PRIMARY KEY (warehouse_id, product_id);

-- add foreign keys
ALTER TABLE `order_client` ADD CONSTRAINT fk_client_fidelity FOREIGN KEY (`type`) REFERENCES order_fidelity(`type`);
ALTER TABLE `order_order` ADD CONSTRAINT fk_order_mail FOREIGN KEY (mail) REFERENCES `order_client`(mail);
ALTER TABLE order_fruit ADD CONSTRAINT fk_fruit_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_vegetable ADD CONSTRAINT fk_vegetable_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_orderdetail ADD CONSTRAINT fk_order_detail_order_id FOREIGN KEY (order_id) REFERENCES `order_order`(order_id);
ALTER TABLE order_orderdetail ADD CONSTRAINT fk_order_detail_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_stock ADD CONSTRAINT fk_stock_warehouse_id FOREIGN KEY (warehouse_id) REFERENCES order_warehouse(warehouse_id);
ALTER TABLE order_stock ADD CONSTRAINT fk_stock_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);