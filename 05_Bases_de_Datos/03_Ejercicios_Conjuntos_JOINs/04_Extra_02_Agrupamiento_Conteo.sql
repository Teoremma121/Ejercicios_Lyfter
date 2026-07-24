-- SQLite
-- Agrupamiento y conteo cruzado

-- Usando las tablas de Books, Customers y Rents:
-- Obtenga el número total de veces que cada cliente ha rentado un libro
-- Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
-- Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT
SELECT
customers.name as Cliente,
COUNT(*) as Rentas_Totales
FROM rents
INNER JOIN books
ON rents.bookID = books.ID
INNER JOIN customers
ON rents.customerID = customers.ID
GROUP BY Cliente
ORDER BY Rentas_Totales DESC
LIMIT 3;