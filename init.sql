-- Active: 1701801198772@@127.0.0.1@3306@fruiticart
USE fruiticart;

DROP TABLE IF EXISTS order_client;
DROP TABLE IF EXISTS order_contact;
DROP TABLE IF EXISTS order_order;
DROP TABLE IF EXISTS order_product;
DROP TABLE IF EXISTS order_fruit;
DROP TABLE IF EXISTS order_vegetable;
DROP TABLE IF EXISTS order_orderdetail;
DROP TABLE IF EXISTS order_warehouse;
DROP TABLE IF EXISTS order_stock;

-- create tables
CREATE TABLE IF NOT EXISTS order_client (
    email VARCHAR(50) NOT NULL PRIMARY KEY,
    `password` VARCHAR(50),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    phone_number VARCHAR(10),
    `address` VARCHAR(50),
    postal_code VARCHAR(5),
    registered_credit_card VARCHAR(16),
);

CREATE TABLE IF NOT EXISTS order_contact (
    contact_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(60),
    email VARCHAR(50),
    `message` VARCHAR(500),
)

CREATE TABLE IF NOT EXISTS order_order (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    delivery_date DATE,
    delivery_option ENUM('Standard','Express'),
    delivery_address VARCHAR(50),
    delivery_postal_code VARCHAR(5),
    `status` ENUM('Pending','Confirmed','In transit','Delivered','Cancelled'),
    total_price DECIMAL(10,2),
    credit_card VARCHAR(16),
    email_id VARCHAR(50) NOT NULL
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
    orderdetail_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
    stock_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    warehouse_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT
);

-- add foreign keys
ALTER TABLE order_contact ADD CONSTRAINT fk_contact_email FOREIGN KEY (email) REFERENCES order_client(email);
ALTER TABLE order_order ADD CONSTRAINT fk_order_mail_id FOREIGN KEY (mail_id) REFERENCES order_client(email);
ALTER TABLE order_fruit ADD CONSTRAINT fk_fruit_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_vegetable ADD CONSTRAINT fk_vegetable_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_orderdetail ADD CONSTRAINT fk_order_detail_order_id FOREIGN KEY (order_id) REFERENCES order_order(order_id);
ALTER TABLE order_orderdetail ADD CONSTRAINT fk_order_detail_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);
ALTER TABLE order_stock ADD CONSTRAINT fk_stock_warehouse_id FOREIGN KEY (warehouse_id) REFERENCES order_warehouse(warehouse_id);
ALTER TABLE order_stock ADD CONSTRAINT fk_stock_product_id FOREIGN KEY (product_id) REFERENCES order_product(product_id);