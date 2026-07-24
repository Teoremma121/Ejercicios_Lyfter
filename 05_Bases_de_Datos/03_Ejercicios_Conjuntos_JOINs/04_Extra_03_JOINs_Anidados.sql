-- SQLite
-- Consulta con múltiples JOINS anidados

-- Genere un SELECT que devuelva lo siguiente:
-- Nombre del cliente
-- Nombre del libro
-- Nombre del autor
-- Estado del alquiler (Rents.State)
-- Debe manejar el caso en que un libro no tenga autor

SELECT
customers.name AS Cliente,
books.name AS Libro,
authors.name AS Autor,
rents.state AS Estado_del_Alquiler
FROM rents
LEFT JOIN books
ON rents.bookID = books.ID
LEFT JOIN authors
ON books.author = authors.ID
LEFT JOIN customers
ON rents.customerID = customers.ID;