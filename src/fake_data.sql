-- Active: 1723480263563@@127.0.0.1@3306

-- USER 
INSERT INTO USER (name, address, phone_number, email_address, membership_type, user_role, account_status, password)
VALUES
('Alice Johnson', '123 Main St', '1234567890', 'alice@example.com', 'Public', 'Member', 'Active', 'password123'),
('Bob Smith', '456 Elm St', '2345678901', 'bob@example.com', 'Public', 'Member', 'Active', 'password123'),
('Charlie Brown', '789 Oak St', '3456789012', 'charlie@example.com', 'Public', 'Librarian', 'Active', 'password123'),
('Diana Prince', '101 Maple St', '4567890123', 'diana@example.com', 'Public', 'Member', 'Active', 'password123'),
('Edward Nigma', '202 Pine St', '5678901234', 'edward@example.com', 'Premium', 'Member', 'Inactive', 'password123'),
('Fiona Glenanne', '303 Cedar St', '6789012345', 'fiona@example.com', 'Public', 'Member', 'Active', 'password123'),
('George O’Malley', '404 Birch St', '7890123456', 'george@example.com', 'Public', 'Librarian', 'Active', 'password123'),
('Hank Pym', '505 Spruce St', '8901234567', 'hank@example.com', 'Public', 'Member', 'Active', 'password123'),
('Iris West', '606 Willow St', '9012345678', 'iris@example.com', 'Premium', 'Member', 'Active', 'password123'),
('Jack Ryan', '707 Redwood St', '0123456789', 'jack@example.com', 'Public', 'Member', 'Active', 'password123');


-- AUTHOR 
INSERT INTO AUTHOR (name)
VALUES
('F. Scott Fitzgerald'),
('Harper Lee'),
('George Orwell'),
('J.D. Salinger'),
('Cormac McCarthy'),
('Jane Austen'),
('Ray Bradbury'),
('Dan Brown'),
('Gabriel Garcia Marquez'),
('Herman Melville'),
('Neil Gaiman'),
('Terry Pratchett');


-- BOOK_GENRES
INSERT INTO BOOK_GENRES (ISBN, genre)
VALUES
('978-3-16-148410-0', 'Classic'),
('978-0-7432-7356-5', 'Historical'),
('978-0-452-28423-4', 'Dystopian'),
('978-0-553-21311-7', 'Classic'),
('978-0-316-76948-0', 'Post-Apocalyptic'),
('978-0-141-03019-2', 'Romance'),
('978-0-452-27750-3', 'Science Fiction'),
('978-0-7432-7357-2', 'Thriller'),
('978-0-140-44255-5', 'Satire'),
('978-0-7434-8623-4', 'Fantasy'),
('978-0-06-085398-3', 'Fantasy');


-- BOOK_AUTHOR
INSERT INTO BOOK_AUTHOR (ISBN, author_id)
VALUES
('978-3-16-148410-0', 1),
('978-0-7432-7356-5', 2),
('978-0-452-28423-4', 3),
('978-0-553-21311-7', 4),
('978-0-316-76948-0', 5),
('978-0-141-03019-2', 6),
('978-0-452-27750-3', 7),
('978-0-7432-7357-2', 8),
('978-0-140-44255-5', 9),
('978-0-7434-8623-4', 10),
('978-0-06-085398-3', 11),
('978-0-06-085398-3', 12);


-- BOOK 
INSERT INTO BOOK (ISBN, title, publisher, edition, publication_date, language, number_of_copies_available, book_cover_image, description)
VALUES
('978-3-16-148410-0', 'The Great Gatsby', 'Scribner', 1, '1925-04-10', 'English', 5, 'https://m.media-amazon.com/images/I/61EtTpQI3vL._SY342_.jpg', 'A novel set in the Jazz Age on Long Island, focusing on the mysterious millionaire Jay Gatsby.'),
('978-0-7432-7356-5', 'To Kill a Mockingbird', 'J.B. Lippincott & Co.', 1, '1960-07-11', 'English', 3, 'https://m.media-amazon.com/images/I/81aY1lxk+9L._SY342_.jpg', 'A story of racial injustice and childhood innocence set in the American South.'),
('978-0-452-28423-4', '1984', 'Secker & Warburg', 1, '1949-06-08', 'English', 8, 'https://m.media-amazon.com/images/I/71rpa1-kyvL._SY342_.jpg', 'A dystopian novel that explores the dangers of totalitarianism.'),
('978-0-553-21311-7', 'The Catcher in the Rye', 'Little, Brown and Company', 1, '1951-07-16', 'English', 7, 'https://m.media-amazon.com/images/I/8125BDk3l9L._SY342_.jpg', 'A novel about teenage rebellion and angst, narrated by the cynical Holden Caulfield.'),
('978-0-316-76948-0', 'The Road', 'Alfred A. Knopf', 1, '2006-09-26', 'English', 6, 'https://m.media-amazon.com/images/I/51M7XGLQTBL._SY342_.jpg', 'A post-apocalyptic tale of a father and son journeying through a desolate America.'),
('978-0-141-03019-2', 'Pride and Prejudice', 'T. Egerton', 1, '1813-01-28', 'English', 10, 'https://m.media-amazon.com/images/I/81a3sr-RgdL._SY342_.jpg', 'A romantic novel that deals with issues of class, marriage, and morality in 19th-century England.'),
('978-0-452-27750-3', 'Fahrenheit 451', 'Ballantine Books', 1, '1953-10-19', 'English', 4, 'https://m.media-amazon.com/images/I/61l8LHt4MeL._SY342_.jpg', 'A novel set in a future where books are banned and "firemen" burn any that are found.'),
('978-0-7432-7357-2', 'The Da Vinci Code', 'Doubleday', 1, '2003-03-18', 'English', 9, 'https://m.media-amazon.com/images/I/811nqCf7o1L._SY342_.jpg', 'A mystery thriller that explores an alternative religious history through art and symbology.'),
('978-0-140-44255-5', 'Animal Farm', 'Secker & Warburg', 1, '1945-08-17', 'English', 12, 'https://m.media-amazon.com/images/I/71je3-DsQEL._SY342_.jpg', 'A satirical novella reflecting events leading up to the Russian Revolution of 1917 and then on into the Stalinist era of the Soviet Union.'),
('978-0-7434-8623-4', 'The Hobbit', 'George Allen & Unwin', 1, '1937-09-21', 'English', 15, 'https://m.media-amazon.com/images/I/418jD+Rsd5L._SY445_SX342_.jpg', 'A fantasy novel about the journey of Bilbo Baggins, a hobbit who is reluctantly drawn into an adventure to recover treasure guarded by a dragon.'),
('978-0-06-085398-3', 'Good Omens', 'William Morrow', 1, '1990-05-01', 'English', 5, 'https://m.media-amazon.com/images/I/61nwsm+zAxL._SY342_.jpg', 'A comedic novel about the birth of the son of Satan and the coming of the End Times.');


-- For "The Great Gatsby" (5 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-3-16-148410-0', 'A1', 'Available'),
('978-3-16-148410-0', 'A2', 'Available'),
('978-3-16-148410-0', 'A3', 'Available'),
('978-3-16-148410-0', 'A4', 'Available'),
('978-3-16-148410-0', 'A5', 'Available');

-- For "To Kill a Mockingbird" (3 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-7432-7356-5', 'B1', 'Available'),
('978-0-7432-7356-5', 'B2', 'Checked Out'),
('978-0-7432-7356-5', 'B3', 'Available');

-- For "1984" (8 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-452-28423-4', 'C1', 'Available'),
('978-0-452-28423-4', 'C2', 'Available'),
('978-0-452-28423-4', 'C3', 'Available'),
('978-0-452-28423-4', 'C4', 'Available'),
('978-0-452-28423-4', 'C5', 'Available'),
('978-0-452-28423-4', 'C6', 'Available'),
('978-0-452-28423-4', 'C7', 'Available'),
('978-0-452-28423-4', 'C8', 'Available');

-- For "The Catcher in the Rye" (7 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-553-21311-7', 'D1', 'Available'),
('978-0-553-21311-7', 'D2', 'Available'),
('978-0-553-21311-7', 'D3', 'Available'),
('978-0-553-21311-7', 'D4', 'Available'),
('978-0-553-21311-7', 'D5', 'Available'),
('978-0-553-21311-7', 'D6', 'Available'),
('978-0-553-21311-7', 'D7', 'Reserved');

-- For "The Road" (6 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-316-76948-0', 'E1', 'Available'),
('978-0-316-76948-0', 'E2', 'Available'),
('978-0-316-76948-0', 'E3', 'Available'),
('978-0-316-76948-0', 'E4', 'Available'),
('978-0-316-76948-0', 'E5', 'Available'),
('978-0-316-76948-0', 'E6', 'Available');

-- For "Pride and Prejudice" (10 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-141-03019-2', 'F1', 'Available'),
('978-0-141-03019-2', 'F2', 'Available'),
('978-0-141-03019-2', 'F3', 'Available'),
('978-0-141-03019-2', 'F4', 'Available'),
('978-0-141-03019-2', 'F5', 'Available'),
('978-0-141-03019-2', 'F6', 'Damaged'),
('978-0-141-03019-2', 'F7', 'Available'),
('978-0-141-03019-2', 'F8', 'Available'),
('978-0-141-03019-2', 'F9', 'Available'),
('978-0-141-03019-2', 'F10', 'Available');

-- For "Fahrenheit 451" (4 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-452-27750-3', 'G1', 'Available'),
('978-0-452-27750-3', 'G2', 'Available'),
('978-0-452-27750-3', 'G3', 'Available'),
('978-0-452-27750-3', 'G4', 'Available');

-- For "The Da Vinci Code" (9 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-7432-7357-2', 'H1', 'Available'),
('978-0-7432-7357-2', 'H2', 'Available'),
('978-0-7432-7357-2', 'H3', 'Available'),
('978-0-7432-7357-2', 'H4', 'Available'),
('978-0-7432-7357-2', 'H5', 'Available'),
('978-0-7432-7357-2', 'H6', 'Available'),
('978-0-7432-7357-2', 'H7', 'Available'),
('978-0-7432-7357-2', 'H8', 'Available'),
('978-0-7432-7357-2', 'H9', 'Available');

-- For "Animal Farm" (12 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-140-44255-5', 'I1', 'Available'),
('978-0-140-44255-5', 'I2', 'Available'),
('978-0-140-44255-5', 'I3', 'Available'),
('978-0-140-44255-5', 'I4', 'Available'),
('978-0-140-44255-5', 'I5', 'Available'),
('978-0-140-44255-5', 'I6', 'Available'),
('978-0-140-44255-5', 'I7', 'Available'),
('978-0-140-44255-5', 'I8', 'Available'),
('978-0-140-44255-5', 'I9', 'Available'),
('978-0-140-44255-5', 'I10', 'Available'),
('978-0-140-44255-5', 'I11', 'Available'),
('978-0-140-44255-5', 'I12', 'Available');

-- For "The Hobbit" (15 copies available)
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-7434-8623-4', 'J1', 'Available'),
('978-0-7434-8623-4', 'J2', 'Available'),
('978-0-7434-8623-4', 'J3', 'Available'),
('978-0-7434-8623-4', 'J4', 'Available'),
('978-0-7434-8623-4', 'J5', 'Available'),
('978-0-7434-8623-4', 'J6', 'Available'),
('978-0-7434-8623-4', 'J7', 'Available'),
('978-0-7434-8623-4', 'J8', 'Available'),
('978-0-7434-8623-4', 'J9', 'Available'),
('978-0-7434-8623-4', 'J10', 'Available'),
('978-0-7434-8623-4', 'J11', 'Available'),
('978-0-7434-8623-4', 'J12', 'Available'),
('978-0-7434-8623-4', 'J13', 'Available'),
('978-0-7434-8623-4', 'J14', 'Available'),
('978-0-7434-8623-4', 'J15', 'Available');


-- Finally, let's add 5 copies of "Good Omens" to the BOOK_COPY table.
INSERT INTO BOOK_COPY (ISBN, shelf_location, book_status)
VALUES
('978-0-06-085398-3', 'K1', 'Available'),
('978-0-06-085398-3', 'K2', 'Available'),
('978-0-06-085398-3', 'K3', 'Available'),
('978-0-06-085398-3', 'K4', 'Available'),
('978-0-06-085398-3', 'K5', 'Available');


-- RESERVATION
INSERT INTO RESERVATION (book_id, borrower_id, reservation_date, expiration_date, reservation_status)
VALUES
(2, 1, '2024-08-01', '2024-08-10', 'Active'),
(3, 2, '2024-08-02', '2024-08-11', 'Active'),
(4, 3, '2024-08-03', '2024-08-12', 'Expired'),
(5, 4, '2024-08-04', '2024-08-13', 'Active'),
(6, 5, '2024-08-05', '2024-08-14', 'Active'),
(7, 6, '2024-08-06', '2024-08-15', 'Cancelled'),
(8, 7, '2024-08-07', '2024-08-16', 'Active'),
(9, 8, '2024-08-08', '2024-08-17', 'Active'),
(10, 9, '2024-08-09', '2024-08-18', 'Active'),
(1, 10, '2024-08-10', '2024-08-19', 'Active');


-- DEPOSIT
INSERT INTO DEPOSIT (borrower_id, book_id, issue_date, due_date, return_date, overdue_fines, renewal_status)
VALUES
(1, 1, '2024-07-01', '2024-07-10', '2024-07-09', 0, 'First-time'),
(2, 2, '2024-07-02', '2024-07-11', '2024-07-12', 5, 'Renewed'),
(3, 3, '2024-07-03', '2024-07-12', '2024-07-10', 0, 'First-time'),
(4, 4, '2024-07-04', '2024-07-13', NULL, 10, 'Overdue'),
(5, 5, '2024-07-05', '2024-07-14', '2024-07-13', 0, 'First-time'),
(6, 6, '2024-07-06', '2024-07-15', '2024-07-14', 0, 'First-time'),
(7, 7, '2024-07-07', '2024-07-16', '2024-07-15', 0, 'First-time'),
(8, 8, '2024-07-08', '2024-07-17', NULL, 0, 'Renewed'),
(9, 9, '2024-07-09', '2024-07-18', '2024-07-17', 0, 'First-time'),
(10, 10, '2024-07-10', '2024-07-19', NULL, 0, 'Renewed');


-- GENRE
INSERT INTO GENRE (genre, description)
VALUES
('Classic', 'Timeless works of literature that have been revered through the ages.'),
('Historical', 'Works of fiction set in a historical period.'),
('Dystopian', 'Depicts an imagined society that is dehumanizing and frightening.'),
('Post-Apocalyptic', 'Stories set after a major, civilization-ending catastrophe.'),
('Romance', 'Novels focusing on romantic relationships.'),
('Science Fiction', 'Fiction based on imagined future scientific discoveries.'),
('Thriller', 'Books that are full of suspense and excitement.'),
('Satire', 'Literature that uses humor and irony to criticize or mock.'),
('Fantasy', 'Fiction that includes magical or supernatural elements.'),
('Mystery', 'Stories revolving around the solving of a crime or unraveling secrets.');


-- MEMBERSHIP_TYPE
INSERT INTO MEMBERSHIP_TYPE (type, description)
VALUES
('Public', 'Basic membership allowing borrowing of standard books.'),
('Premium', 'Upgraded membership with access to exclusive content and extended borrowing privileges.');


-- USER_ROLE
INSERT INTO USER_ROLE (role, description)
VALUES
('Member', 'Regular user with borrowing privileges.'),
('Librarian', 'Staff responsible for managing the library and assisting members.');


-- BOOK_STATUS
INSERT INTO BOOK_STATUS (status, description)
VALUES
('Available', 'Book is available for borrowing.'),
('Checked Out', 'Book is currently borrowed.'),
('Reserved', 'Book is reserved by a user.'),
('Damaged', 'Book is damaged and not available for borrowing.');


-- RESERVATION_STATUS
INSERT INTO RESERVATION_STATUS (status, description)
VALUES
('Active', 'Reservation is currently active.'),
('Expired', 'Reservation has expired.'),
('Cancelled', 'Reservation was cancelled.');


-- RENEWAL_STATUS
INSERT INTO RENEWAL_STATUS (status, description)
VALUES
('First-time', 'The book has not been renewed yet.'),
('Renewed', 'The book has been renewed.'),
('Overdue', 'The book is overdue and has not been returned.');
