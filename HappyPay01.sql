CREATE DATABASE happypay;

USE happypay;

CREATE TABLE transactions (user_name VARCHAR(200),user_birth_date VARCHAR(200),user_birth_city VARCHAR(200),seller VARCHAR(200),seller_address VARCHAR(200),transaction_amount VARCHAR(200),transaction_date VARCHAR(200));

SELECT * FROM transactions;

SELECT COUNT(*) FROM transactions;

SELECT transaction_amount FROM transactions;

SELECT MAX(transaction_amount) FROM transactions;

ALTER TABLE transactions MODIFY COLUMN transaction_amount DECIMAL(8, 2);

SELECT MAX(transaction_amount) FROM transactions;