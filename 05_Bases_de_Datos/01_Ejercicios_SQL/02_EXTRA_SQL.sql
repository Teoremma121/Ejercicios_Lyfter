-- SQLite
-- 1. Crear categorías y ajustar productos
-- Cree la tabla categories con:
-- id (PK autoincrement)
-- name (UNIQUE, NOT NULL)
-- description
DROP TABLE categories;
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name VARCHAR(25) NOT NULL UNIQUE,
    description VARCHAR(40)
);

-- Agregue a products la columna category_id (INTEGER, puede permitir NULL)
ALTER TABLE products
    ADD COLUMN category_id INTEGER REFERENCES categories(id);

-- Inserte al menos 3 filas en categories
INSERT INTO categories (name, description)
    VALUES
    ('COLLAB', 'Collaboration with any external franchise'),
    ('KIDS', 'designed for children'),
    ('ART', 'collectionable items');

-- Actualice algunos products asignándoles un category_id
UPDATE products
    SET
        category_id = CASE id
        WHEN 1 THEN 2
        WHEN 3 THEN 3
        WHEN 4 THEN 1
        WHEN 6 THEN 1
        WHEN 8 THEN 3
        END
        WHERE id IN (1,3,4,6,8);

-- Verifique con SELECT * FROM products (muestre id, product_name, price, category_id, stock_available)
SELECT * FROM products;

-- 2. Carga de productos y filtros básicos
-- Inserte al menos 10 filas en products con product_name, price, stock_available
INSERT INTO products (code, name, price, brand, entry_date, stock_available)
    VALUES
    ('60431', 'Space Explorer Rover', 34.99, 'CITY', '2025-01-01', 11),
    ('43247', 'Young Simba', 129.99, 'DISNEY', '2024-06-01', 13),
    ('71820', 'Kai''s Dragon Spinjitzu Spinner', -9.99, 'NINJAGO', '2024-01-01', 9),
    ('71489', 'Cooper''s Robot Dinosaur C-Rex', 89.99, 'DREAMZZZ', '2025-01-01', 7),
    ('10353', 'Williams Racing FW14B & Nigel Mansell', 79.99, 'ICONS', '2025-03-01', 11),
    ('40782', 'Apple Harvest Festival', 24.99, 'SEASONAL', '2025-09-01', 12),
    ('40783', 'Apple Orchard Picnic', 19.99, 'SEASONAL', '2025-09-01', 10),
    ('76444', 'Diagon Alley: Wizarding Shops', 199.99, 'HARRY POTTER', '2025-01-01', 6),
    ('77054', 'Dodo Airlines Airport', 37.99, 'ANIMAL CROSSING', '2024-08-01', 15),
    ('42665', 'Puppy Playground Adventure', 14.99, 'FRIENDS', '2025-01-01', 17);

-- Seleccione todos los productos
SELECT * FROM products;

-- Seleccione productos con price > 50000
SELECT *
    FROM products
    WHERE price*456.28 > 50000;
    
-- Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE
SELECT *
    FROM products
    WHERE name LIKE '%apple%';
-- Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5
SELECT *
    FROM products
    ORDER BY price DESC
    LIMIT 5;

-- 3. Correcciones de datos en productos
-- Establezca stock_available = 0 donde price <= 0
UPDATE products
    SET stock_available = 0
    WHERE price <= 0;

-- Aumente el price en 100 unidades para todos los productos cuando stock_available sea menor a 10
UPDATE products
    SET price = price + (100/456.28)
    WHERE stock_available < 10;

-- Disminuya stock_available en 1 para un product_id específico
UPDATE products
    SET stock_available = stock_available - 1
    WHERE id = 20;

-- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
SELECT * FROM products ORDER BY id ASC;
