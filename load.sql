-- Active: 1701801198772@@127.0.0.1@3306@fruiticart
USE fruiticart;

INSERT INTO `order_client` (email, `password`, first_name, last_name, phone_number, `address`, postal_code, registered_credit_card) VALUES 
('test@test', 'test', 'testFName', 'testLName', '0123456789', 'testAddress', '12345', '1234567891234567'),
('john.doe@email.com', 'motdepasse1', 'John', 'Doe', '1234567890', '123 Rue des Fleurs', '75001', '1234567891234567'),
('jane.smith@email.com', 'motdepasse2', 'Jane', 'Smith', '9876543210', '456 Avenue des Étoiles', '75002', '1234567891234567'),
('alice.johnson@email.com', 'motdepasse3', 'Alice', 'Johnson', '5556667777', '789 Boulevard du Soleil', '75003', '1234567891234567'),
('bob.williams@email.com', 'motdepasse4', 'Bob', 'Williams', '3332221111', '1010 Rue de la Lune', '75004', '1234567891234567'),
('emma.martin@email.com', 'motdepasse5', 'Emma', 'Martin', '9998887777', '2020 Avenue des Nuages', '75005', '1234567891234567'),
('charlie.brown@email.com', 'motdepasse6', 'Charlie', 'Brown', '1110009999', '303 Rue des Montagnes', '75006', '1234567891234567'),
('olivia.white@email.com', 'motdepasse7', 'Olivia', 'White', '7776665555', '404 Avenue des Rivières', '75007', '1234567891234567'),
('michael.davis@email.com', 'motdepasse8', 'Michael', 'Davis', '4443332222', '505 Boulevard des Forêts', '75008', '1234567891234567'),
('sophia.thomas@email.com', 'motdepasse9', 'Sophia', 'Thomas', '2221110000', '606 Rue des Champs', '75009', '1234567891234567'),
('liam.jackson@email.com', 'motdepasse10', 'Liam', 'Jackson', '8887776666', '707 Avenue des Plaines', '75010', '1234567891234567');

INSERT INTO `order_order` (order_id, order_date, delivery_date, delivery_option, delivery_address, delivery_postal_code, `status`, total_price, credit_card, email_id) VALUES 
(1, '2021-01-01', '2021-01-03', 'Express', '123 Rue des Fleurs', '75001', 'Delivered', 10.70, '1234567891234567', 'john.doe@email.com'),
(2, '2023-01-01', '2023-01-05', 'Standard', '123 Rue des Fleurs', '75001', 'Delivered', 14.32, '1234567891234567', 'john.doe@email.com'),
(3, '2022-04-28', '2022-04-30', 'Standard', '456 Avenue des Étoiles', '75002', 'Delivered', 12.50, '1234567891234567', 'jane.smith@email.com'),
(4, '2022-10-13', '2022-10-17', 'Standard', '456 Avenue des Étoiles', '75002', 'Delivered', 34.12, '1234567891234567', 'jane.smith@email.com'),
(5, '2021-12-24', '2021-12-26', 'Express', '1010 Rue de la Lune', '75004', 'Delivered', 15.00, '1234567891234567', 'bob.williams@email.com'),
(6, '2023-10-21', '2023-10-25', 'Standard', '2020 Avenue des Nuages', '75005', 'Delivered', 9.89, '1234567891234567', 'emma.martin@email.com'),
(7, '2022-11-11', '2022-11-13', 'Standard', '303 Rue des Montagnes', '75006', 'Cancelled', 8.99, '1234567891234567', 'charlie.brown@email.com'),
(8, '2022-12-12', '2022-12-14', 'Standard', '404 Avenue des Rivières', '75007', 'Delivered', 7.99, '1234567891234567', 'olivia.white@email.com'),
(9, '2023-05-15', '2023-05-20', 'Standard', '404 Avenue des Rivières', '75007', 'Delivered', 39.47, '1234567891234567', 'olivia.white@email.com'),
(10, '2023-06-16', '2023-06-18', 'Standard', '505 Boulevard des Forêts', '75008', 'Cancelled', 12.50, '1234567891234567', 'michael.davis@email.com'),
(11, '2023-07-17', '2023-07-19', 'Express', '606 Rue des Champs', '75009', 'Delivered', 21.01, '1234567891234567', 'sophia.thomas@email.com'),
(12, '2023-08-18', '2023-08-20', 'Standard', '707 Avenue des Plaines', '75010', 'Delivered', 10.00, '1234567891234567', 'liam.jackson@email.com');

INSERT INTO order_product (product_id) VALUES 
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20);

INSERT INTO order_fruit (fruit_id, `name`, price, origin, product_id) VALUES 
(1, 'Apple', 1.99, 'France', 1),
(2, 'Banana', 1.99, 'Spain', 2),
(3, 'Orange', 1.64, 'Italy', 3),
(4, 'Pear', 2.69, 'France', 4),
(5, 'Pineapple', 3.99, 'Spain', 5),
(6, 'Strawberry', 4.58, 'Italy', 6),
(7, 'Cherry', 11.99, 'France', 7),
(8, 'Grape', 6.00, 'Spain', 8),
(9, 'Lemon', 2.98, 'Italy', 9),
(10, 'Watermelon', 4.79, 'France', 10),
(11, 'Kiwi', 2.99, 'Spain', 11),
(12, 'Peach', 2.99, 'Italy', 12);

INSERT INTO order_vegetable (vegetable_id, `name`, price, origin, product_id) VALUES 
(1, 'Carrot', 1.39, 'France', 13),
(2, 'Cucumber', 1.69, 'Spain', 14),
(3, 'Tomato', 1.00, 'Italy', 15),
(4, 'Potato', 0.99, 'France', 16),
(5, 'Onion', 2.69, 'Spain', 17),
(6, 'Garlic', 4.09, 'Italy', 18),
(7, 'Pepper',3.99 , 'France', 19),
(8, 'Eggplant', 4.58, 'Spain', 20);

INSERT INTO order_orderdetail (orderdetail_id, order_id, product_id, quantity) VALUES 
(1, 1, 2, 10),
(2, 1, 11, 5),
(3, 2, 19, 7),
(4, 3, 3, 5),
(5, 3, 4, 5),
(6, 4, 5, 10),
(7, 4, 6, 12),
(8, 5, 7, 22),
(9, 6, 9, 13),
(10, 6, 10, 5),
(11, 7, 12, 6),
(12, 7, 13, 12),
(13, 8, 14, 14),
(14, 8, 15, 8),
(15, 8, 4, 9),
(16, 9, 12, 25),
(17, 9, 17, 10),
(18, 10, 9, 17),
(19, 10, 19, 3),
(20, 10, 13, 18),
(21, 11, 20, 14),
(22, 11, 1, 11),
(23, 12, 13, 8),
(24, 12, 3, 5),
(25, 12, 4, 5);

INSERT INTO order_warehouse (warehouse_id, `address`, postal_code, `zone`) VALUES 
(1, '606 Rue des Champs', '75009', 'North'),
(2, '707 Avenue des Plaines', '75010', 'North'),
(3, '808 Boulevard des Vagues', '75011', 'North'),
(4, '909 Rue des Collines', '75012', 'East'),
(5, '1010 Avenue des Chênes', '75013', 'South'),
(6, '1111 Boulevard des Rochers', '75014', 'South'),
(7, '1212 Rue des Vallées', '75015', 'West');