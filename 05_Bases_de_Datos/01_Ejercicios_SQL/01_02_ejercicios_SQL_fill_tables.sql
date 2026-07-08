-- SQLite

INSERT INTO products (code, name, price, brand ,entry_date, stock_available)
	VALUES
        ('41731', 'Heartlake International School', 99.99, 'FRIENDS', '2023-01-01', 1),
        ('71792', 'Sora''s Transforming Mech Bike Racer', 47.99, 'NINJAGO', '2024-01-01', 1),
        ('10316', 'The Lord of the Rings: Rivendell', 499.99, 'ICONS', '2023-03-08', 1),
        ('75379', 'R2-D2', 99.99, 'STAR WARS', '2024-03-01', 1),
        ('42171', 'Mercedes-AMG F1 W14 E Performance', 219.99, 'TECHNIC', '2024-03-01', 1),
        ('76269', 'Avengers Tower', 499.99, 'MARVEL', '2023-11-24', 1),
        ('21338', 'A-Frame Cabin', 179.99, 'IDEAS', '2023-02-04', 0),
        ('10295', 'Porsche 911', 169.99, 'ICONS', '2021-03-01', 0),
        ('31147', 'Retro Camera', 19.99, 'CREATOR 3-in-1', '2024-01-01', 1),
        ('76989', 'Horizon Forbidden West: Tallneck', 89.99, 'HORIZON', '2022-05-01', 0);

INSERT INTO invoices (invoice_number, purchase_date, buyer_email)
        VALUES
        ('INV-202606-1001', '2026-06-02', 'emily.johnson84@gmail.com'),
        ('INV-202606-1002', '2026-06-04', 'michael.smith92@gmail.com'),
        ('INV-202606-1003', '2026-06-06', 'ashley.brown17@gmail.com'),
        ('INV-202606-1004', '2026-06-08', 'christopher.miller55@gmail.com'),
        ('INV-202606-1005', '2026-06-11', 'samantha.wilson03@gmail.com'),
        ('INV-202606-1006', '2026-06-15', 'daniel.anderson78@gmail.com'),
        ('INV-202606-1007', '2026-06-18', 'olivia.thomas26@gmail.com'),
        ('INV-202606-1008', '2026-06-22', 'matthew.moore41@gmail.com'),
        ('INV-202606-1009', '2026-06-26', 'jessica.taylor90@gmail.com'),
        ('INV-202606-1010', '2026-06-29', 'joseph.jackson65@gmail.com');

INSERT INTO invoice_product (invoice_id, product_id, quantity)
        VALUES
        (1,1,2),
        (1,9,1),
        (1,6,1),
        (2,2,2),
        (2,3,3),
        (3,4,2),
        (3,8,1),
        (4,7,1),
        (4,10,2),
        (5,6,3),
        (5,9,1),
        (6,3,2),
        (7,2,1),
        (8,1,3),
        (9,4,1),
        (10,5,2);

UPDATE invoice_product 
SET total_amount = (
        SELECT price FROM products 
        WHERE products.id = invoice_product.product_id
        ) * quantity;

UPDATE invoices 
SET total_amount = (
        SELECT SUM(ip.total_amount)
        FROM invoice_product AS ip
        WHERE ip.invoice_id = invoices.id
        );

INSERT INTO shopping_carts (buyer_email)
        VALUES
        ('emily.johnson84@gmail.com'),
        ('michael.smith92@gmail.com'),
        ('ashley.brown17@gmail.com'),
        ('christopher.miller55@gmail.com'),
        ('samantha.wilson03@gmail.com'),
        ('daniel.anderson78@gmail.com'),
        ('olivia.thomas26@gmail.com'),
        ('matthew.moore41@gmail.com'),
        ('jessica.taylor90@gmail.com'),
        ('joseph.jackson65@gmail.com'),
        ('ethan.walker31@gmail.com'),
        ('madison.harris88@gmail.com'),
        ('noah.martinez14@gmail.com'),
        ('victoria.clark72@gmail.com'),
        ('jacob.lewis59@gmail.com'),
        ('grace.robinson20@gmail.com');

INSERT INTO cart_product (cart_id, product_id, quantity)
        VALUES
        (2,4,1),
        (7,10,1),
        (10,9,3),
        (11,5,1),
        (12,6,2),
        (12,7,1),
        (14,3,3),
        (16,8,1),
        (16,2,2);