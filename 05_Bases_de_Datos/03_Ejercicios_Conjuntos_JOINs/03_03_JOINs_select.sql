-- SQLite
-- Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT 
    books.name as Book,
    authors.name as Author
    FROM books
    LEFT JOIN authors
    ON books.author = authors.ID;

-- Obtenga todos los libros que no tienen autor
SELECT
    books.name as Book
    FROM books
    LEFT JOIN authors
    ON books.author = authors.ID
    WHERE books.author IS NULL;

-- Obtenga todos los autores que no tienen libros
SELECT 
    authors.name as Author
    FROM authors
    LEFT JOIN books
    ON books.author = authors.ID
    WHERE books.name IS NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT
    DISTINCT books.name as Book
    FROM books
    INNER JOIN rents
    ON books.ID = rents.bookID;

-- Obtenga todos los libros que nunca han sido rentados
SELECT
    books.name as Book
    FROM books
    LEFT JOIN rents
    ON books.ID = rents.bookID
    WHERE rents.ID IS NULL;

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT
    customers.name as Customer
    FROM customers
    LEFT JOIN rents
    ON customers.ID = rents.customerID
    WHERE rents.ID IS NULL;

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT
    rents.ID as RentID,
    books.name as Book
    FROM rents
    INNER JOIN books
    ON rents.bookID = books.ID
    WHERE rents.state = 'Overdue';