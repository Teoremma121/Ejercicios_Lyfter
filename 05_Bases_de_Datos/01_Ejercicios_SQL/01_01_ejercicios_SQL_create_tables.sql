-- SQLite

DROP TABLE products;
DROP TABLE invoices;
DROP TABLE shopping_carts;
DROP TABLE invoice_product;
DROP TABLE cart_product;


CREATE TABLE products (
	id INTEGER PRIMARY KEY,
	code CHAR(5) NOT NULL UNIQUE,
	name VARCHAR(50) NOT NULL,
	price FLOAT DEFAULT 0,
	entry_date DATE DEFAULT CURRENT_DATE,
	brand VARCHAR(25),
	stock_available INTEGER DEFAULT 0
);

CREATE TABLE invoices (
	id INTEGER PRIMARY KEY,
	invoice_number CHAR(15) NOT NULL,
	purchase_date DATE DEFAULT CURRENT_DATE,
	buyer_email VARCHAR(50),
	total_amount INTEGER DEFAULT 0
);

CREATE TABLE shopping_carts (
	id INTEGER PRIMARY KEY,
	buyer_email VARCHAR(50) UNIQUE
);

CREATE TABLE invoice_product (
	id INTEGER PRIMARY KEY,
	invoice_id INTEGER REFERENCES invoices(id),
	product_id INTEGER REFERENCES products(id),
	quantity INTEGER DEFAULT 0,
	total_amount INTEGER DEFAULT 0
);

CREATE TABLE cart_product (
	id INTEGER PRIMARY KEY,
	cart_id INTEGER REFERENCES shopping_carts(id),
	product_id INTEGER REFERENCES products(id),
	quantity INTEGER DEFAULT 0
);