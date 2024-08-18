-- GENRE Table
CREATE TABLE GENRE (
    genre VARCHAR(10) PRIMARY KEY,
    description TEXT 
);

-- MEMBERSHIP_TYPE Table
CREATE TABLE MEMBERSHIP_TYPE (
    type VARCHAR(10) PRIMARY KEY,
    description TEXT NOT NULL
);

-- USER_ROLE Table
CREATE TABLE USER_ROLE (
    role VARCHAR(10) PRIMARY KEY,
    description TEXT NOT NULL
);

-- BOOK_STATUS Table
CREATE TABLE BOOK_STATUS (
    status VARCHAR(10) PRIMARY KEY,
    description TEXT NOT NULL
);

-- RESERVATION_STATUS Table
CREATE TABLE RESERVATION_STATUS (
    status VARCHAR(10) PRIMARY KEY,
    description TEXT NOT NULL
);

-- RENEWAL_STATUS Table
CREATE TABLE RENEWAL_STATUS (
    status VARCHAR(10) PRIMARY KEY,
    description TEXT NOT NULL
);


-- USER Table
CREATE TABLE USER (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,   -- HUST ID TEXT
    name TEXT NOT NULL,
    address TEXT DEFAULT 'None',
    phone_number TEXT NOT NULL UNIQUE,
    email_address TEXT NOT NULL UNIQUE,
    membership_type VARCHAR(10) DEFAULT 'Public',
    user_role VARCHAR(10) DEFAULT 'Member',
    account_status VARCHAR(10) DEFAULT 'Active',
    password TEXT NOT NULL,
    FOREIGN KEY (membership_type) REFERENCES MEMBERSHIP_TYPE(type),
    FOREIGN KEY (user_role) REFERENCES USER_ROLE(role)
);

-- AUTHOR Table
CREATE TABLE AUTHOR (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- BOOK Table
CREATE TABLE BOOK (
    ISBN TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    publisher TEXT NOT NULL,
    edition INTEGER NOT NULL,
    publication_date DATE NOT NULL,
    language TEXT NOT NULL,
    number_of_copies_available INTEGER NOT NULL,
    book_cover_image TEXT,
    description TEXT NOT NULL
);

-- BOOK_GENRES Table
CREATE TABLE BOOK_GENRES (
    ISBN TEXT NOT NULL,
    genre VARCHAR(10) NOT NULL,
    PRIMARY KEY (ISBN, genre),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
    FOREIGN KEY (genre) REFERENCES GENRE(genre)
);

-- BOOK_AUTHOR Table
CREATE TABLE BOOK_AUTHOR (
    ISBN TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (ISBN, author_id),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
    FOREIGN KEY (author_id) REFERENCES AUTHOR(ID)
);

-- BOOK_COPY Table
CREATE TABLE BOOK_COPY (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ISBN TEXT NOT NULL,
    shelf_location TEXT NOT NULL UNIQUE,
    book_status VARCHAR(10) DEFAULT 'Available',
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
    FOREIGN KEY (book_status) REFERENCES BOOK_STATUS(status)
);

-- RESERVATION Table
-- RESERVATION Table
CREATE TABLE RESERVATION (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    borrower_id INTEGER NOT NULL,
    reservation_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    reservation_status VARCHAR(10) DEFAULT 'Active',
    FOREIGN KEY (book_id) REFERENCES BOOK_COPY(ID),
    FOREIGN KEY (borrower_id) REFERENCES USER(ID),
    FOREIGN KEY (reservation_status) REFERENCES RESERVATION_STATUS(status)
);


-- DEPOSIT Table
CREATE TABLE DEPOSIT (
    borrower_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    overdue_fines INTEGER DEFAULT 0,
    renewal_status VARCHAR(10) DEFAULT 'First-time',
    PRIMARY KEY (borrower_id, book_id),
    FOREIGN KEY (borrower_id) REFERENCES USER(ID),
    FOREIGN KEY (book_id) REFERENCES BOOK_COPY(ID),
    FOREIGN KEY (renewal_status) REFERENCES RENEWAL_STATUS(status)
);


