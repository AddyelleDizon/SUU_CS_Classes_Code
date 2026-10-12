CREATE TABLE schemalibrary.Book (
    BookID INT PRIMARY KEY,
    BookTitle VARCHAR(255),
    BookReleaseDate DATE,
    Genre VARCHAR(100)
);

CREATE TABLE schemalibrary.Publisher (
    PubID INT PRIMARY KEY,
    PublisherName VARCHAR(255),
    PublisherAddress VARCHAR(255),
    PublisherCity VARCHAR(100),
    PublisherCountry VARCHAR(100)
);

CREATE TABLE schemalibrary.Book_Publish (
    BookID INT,
    PublisherID INT,
    Date_of_publication DATE NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (BookID, PublisherID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID),
    FOREIGN KEY (PublisherID) REFERENCES Publisher(PubID)
);

INSERT INTO schemalibrary.Book (BookID, BookTitle, BookReleaseDate, Genre) VALUES 
(1, 'The Hunger Games', '2008-09-14', 'Sci-Fi'),
(2, 'Divergent', '2011-04-26', 'Sci-Fi'),
(3, 'Harry Potter', '1997-06-26', 'Fantasy'),
(4, 'Animal Farm', '1945-08-17', 'Satire'),
(5, 'The Catcher in the Rye', '1951-07-16', 'Fiction');

INSERT INTO schemalibrary.Publisher (PubID, PublisherName, PublisherAddress, PublisherCity, PublisherCountry) VALUES 
(1, 'Penguin Books', '123 Penguin St', 'New York', 'USA'),
(2, 'HarperCollins', '456 Harper Ave', 'Los Angeles', 'USA'),
(3, 'Random House', '789 Random Rd', 'London', 'UK'),
(4, 'Simon & Schuster', '321 Simon Blvd', 'Chicago', 'USA'),
(5, 'Hachette Book Group', '654 Hachette St', 'Paris', 'France');

INSERT INTO schemalibrary.Book_Publish (BookID, PublisherID, Date_of_publication, Price) VALUES 
(1, 11, '2008-09-14', 15.99),
(2, 22, '2011-04-26', 12.99),
(3, 33, '1997-06-26', 14.99),
(4, 44, '1945-08-17', 18.50),
(5, 55, '1951-07-16', 13.75);

SELECT * FROM Book;
SELECT * FROM Publisher;
SELECT * FROM Book_Publish;





