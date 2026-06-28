-- SQLite

INSERT INTO products (code, name, price, entry_date, brand, stock_available)
	VALUES 
        ('ZAP001', 'Air Runner Pro', 89.99, '2026-06-15', 'Nike', 1),
        ('ZAP002', 'Classic Leather', 74.50, '2026-06-16', 'Reebok', 1),
        ('ZAP003', 'Ultraboost Light', 149.99, '2026-06-17', 'Adidas', 0)


-- Para probar null y default
INSERT INTO products (code, name)
	VALUES ('ZAP011','Plantillas')