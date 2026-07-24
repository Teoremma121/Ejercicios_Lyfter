SET search_path TO Ejercicios_Transactions;
ALTER TABLE users
ALTER COLUMN password TYPE VARCHAR(15);
ALTER TABLE users
ALTER COLUMN username TYPE VARCHAR(20);
ALTER TABLE products
ALTER COLUMN price TYPE REAL;

-- Users
INSERT INTO users (username, email, password) 
VALUES 
('hello_kitty_bows', 'kitty.white@sanriomail.com','B0w3s&AppIeP1e!'),
('fluffy_cinnamoroll', 'cinnamoroll.cloud@sanriomail.com','C1nn4m0n_R0ll3s'),
('kuromi_goth_vibes','kuromi.skull@sanriomail.com','D4rk_Ch3rry2026'),
('sweet_mymelody','mymelody.hood@sanriomail.com','P1nkH00d_Sw33t!'),
('pompom_pudding','purin.beret@sanriomail.com','Y3ll0w_Pudd1ng#');

-- Products
INSERT INTO products (name, stock, price) 
VALUES 
("Mama's Apple Pie", 3, 6.50),
('Strawberry Cloud Shortcake', 5, 5.75),
('Black Forest Skull Cake', 2, 7.00),
('Golden Pudding Tart', 5, 5.25),
('Pink Almond Blossom Cake', 2, 6.25),
('TROPICAL Magma Cake', 0, 7.50),
('Starry Moonlit Cheesecake', 3, 6.75),
('Matcha Frog Pond Cake', 6, 5.50),
('Under the Sea Coral Tart', 5, 6.00),
('Badtz-Maru Rock Roll Cake', 8, 5.00);

