-- SQLite
-- 1. Obtenga todos los productos almacenados
SELECT *
    FROM products;

-- 2. Obtenga todos los productos que tengan un precio mayor a 50000
SELECT *
    FROM products
    WHERE price*456.28 >= 50000;

-- 3. Obtenga todas las compras de un mismo producto por id.
SELECT *
    FROM invoice_product
    WHERE product_id = 3;

-- 4. Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT
    product_id,
    SUM(total_amount) AS total_per_product
    FROM invoice_product
    GROUP BY product_id;

-- 5. Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
    FROM invoices
    WHERE buyer_email = 'daniel.anderson78@gmail.com';

-- 6. Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
    FROM invoices
    ORDER BY total_amount DESC;

-- 7. Obtenga una sola factura por número de factura.
SELECT *
    FROM invoices
    WHERE invoice_number = 'INV-202606-1008';