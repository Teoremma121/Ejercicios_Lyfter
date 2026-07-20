-- SQLite

INSERT INTO books (name, author)
	VALUES
        ('Don Quijote',1),
        ('La Divina Comedia',2),
        ('Vagabond 1-3',3),
        ('Dragon Ball 1',4),
        ('The Book of the 5 Rings',NULL);

INSERT INTO authors (name)
	VALUES
        ('Miguel de Cervantes'),
        ('Dante Alighieri'),
        ('Takehiko Inoue'),
        ('Akira Toriyama'),
        ('Walt Disney');

INSERT INTO customers (name, email)
        VALUES
        ('John Doe', 'j.doe@email.com'),
        ('Jane Doe', 'jane@doe.com'),
        ('Luke Skywalker', 'darth.son@email.com');

INSERT INTO rents (bookID, customerID, state)
        VALUES
        (1,2,'Returned'),
        (2,2,'Returned'),
        (1,1,'On time'),
        (3,1,'On time'),
        (2,2,'Overdue');