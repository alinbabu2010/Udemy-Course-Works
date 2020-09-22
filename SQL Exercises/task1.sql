CREATE TABLE categories(
	category_name VARCHAR(10),
	PRIMARY KEY(category_name)
);
CREATE TABLE products(
	product_id INT,
	product_name VARCHAR(20),
	category_name VARCHAR(10),
	price INT,
	PRIMARY KEY(product_id),
	FOREIGN KEY(category_name) REFERENCES categories(category_name)
);
CREATE TABLE users(
	user_id INT,
	email VARCHAR(50),
	user_name VARCHAR(20),
	age INT,
	PRIMARY KEY(user_id)
);
CREATE TABLE purchase(
	user_id INT,
	product_id INT,
	quantity INT,
	total_price INT,
	purchase_date DATE,
	PRIMARY KEY(user_id,product_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id),
	FOREIGN KEY(product_id) REFERENCES products(product_id)
);
INSERT INTO categories(category_name) VALUES(
	'Soap'),
	('Cereals'),
	('Biscuit'),
	('Pen'),
	('Pencil');
INSERT INTO products VALUES(
	101,'Lux','Soap',20),
	(102,'Wheat','Cereals',75),
	(103,'Tiger','Biscuit','20'),
	(104,'Cinthol','Soap',25),
	(105,'Nataraj','Pencil',3),
	(106,'Cello','Pen','10');
INSERT INTO users VALUES(
	101,'ajay@yahoo.com','Ajay',25),
	(102,'arun12@google.com','Arun',37),
	(103,'alice@google.com','Alice',40);
INSERT INTO purchase VALUES(
	103,102,5,375,'09-Feb-2020'),
	(103,103,1,20,'08-Mar-2020'),
	(103,101,3,60,'15-Mar-2020'),
	(102,106,10,100,'12-Feb-2020'),
	(101,104,2,40,'05-Mar-2020'),
	(102,102,2,150,'30-Mar-2020');

/* Fetch all products under a category */
SELECT * FROM products WHERE category_name='Soap';

/*Fetch sum of price of all products under a category*/
SELECT SUM(price) FROM products WHERE category_name='Soap';

/*Fetch total amount purchased by a user*/
SELECT user_id,SUM(total_price) FROM purchase GROUP BY user_id;
SELECT SUM(total_price) FROM purchase WHERE user_id=103;

/*Fetch all purchases after a specific date*/
SELECT * FROM purchase WHERE purchase_date > '05-Mar-2020';

/*Most selled category.*/
SELECT  s.category_name FROM products s  JOIN purchase u ON s.product_id=u.product_id GROUP BY s.category_name ORDER BY SUM(u.quantity) DESC LIMIT 1;

/*Find the Customer who brought most products in each category.*/
SELECT user_name,category_name FROM purchase  NATURAL JOIN products NATURAL JOIN users GROUP BY user_name,category_name ORDER BY SUM(quantity) DESC;

/*Find the Customer who brought for maximum amount in a specific date range*/
SELECT user_name FROM purchase NATURAL JOIN users WHERE total_price IN (SELECT MAX(total_price) FROM purchase WHERE purchase_date BETWEEN '01-Mar-2020' AND '31-Mar-2020');

/*Find the purchase details of a user on a specific date*/
SELECT * FROM purchase NATURAL JOIN users WHERE purchase_date='12-Feb-2020' AND user_id='102';