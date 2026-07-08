-- SQLite
-- Utilizando el comando ALTER, modifique la tabla de Facturas y 
-- agregue una columna para almacenar también el número de teléfono del comprador,
-- y otra para el código de empleado del cajero que realizó la venta.


ALTER TABLE invoices
    ADD COLUMN buyer_number VARCHAR(17);

ALTER TABLE invoices
    ADD COLUMN cashier_code VARCHAR(11);

UPDATE invoices
    SET
        buyer_number = CASE id
        WHEN 1 THEN '+1 (212) 555-0148'
        WHEN 2 THEN '+1 (310) 555-0273'
        WHEN 3 THEN '+1 (415) 555-0391'
        WHEN 4 THEN '+1 (617) 555-0416'
        WHEN 5 THEN '+1 (305) 555-0529'
        WHEN 6 THEN '+1 (404) 555-0634'
        WHEN 7 THEN '+1 (702) 555-0741'
        WHEN 8 THEN '+1 (206) 555-0857'
        WHEN 9 THEN '+1 (512) 555-0962'
        WHEN 10 THEN '+1 (718) 555-1078'
        END,

        cashier_code = CASE id
        WHEN 1 THEN 'EMP-24-0187'
        WHEN 2 THEN 'EMP-25-0342'
        WHEN 3 THEN 'EMP-26-0059'
        WHEN 4 THEN 'EMP-26-0059'
        WHEN 5 THEN 'EMP-26-0059'
        WHEN 6 THEN 'EMP-24-0187'
        WHEN 7 THEN 'EMP-24-0187'
        WHEN 8 THEN 'EMP-25-0342'
        WHEN 9 THEN 'EMP-24-0187'
        WHEN 10 THEN 'EMP-25-0342'
        END

        WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);