# Entity Relationship Diagrams

All entities might be appear:
1. Book
2. Author
3. Reader
4. Librarian

```mermaid
---
    title: Library Database
---
erDiagram
    GENRE {
        VARCHAR(50) genre PK
        TEXT description
    }

    MEMBERSHIP_TYPE {
        %% Available Type: "Public || Premium"
        VARCHAR(50) type PK
        TEXT description NOT NULL
    }

    USER_ROLE {
        %% Available role: "Librarian || Member"
        VARCHAR(50) role PK
        TEXT description NOT NULL
    }

    BOOK_STATUS {
        %% Available status: "Available || Checked Out || Reserved || Damaged"
        VARCHAR(50) status PK
        TEXT description NOT NULL
    }

    RESERVATION_STATUS {
        %% Available status: "Active || Expired || Cancelled"
        VARCHAR(50) status PK
        TEXT description NOT NULL
    }

    RENEWAL_STATUS {
        %% Available status: "First-time || Renewed || Overdue"
        VARCHAR(50) status PK
        TEXT description NOT NULL
    }

    USER {
        INTEGER ID PK   "HUST-ID 8 digits from 2016 to 2024"       
        TEXT name "NOT NULL"
        TEXT address
        TEXT phone_number "NOT NULL UNIQUE   Must contain 10 digits"
        TEXT email_address "NOT NULL UNIQUE   Ex: *@gmail.com"
        VARCHAR(50) membership_type FK       "DEFAULT Public"
        VARCHAR(50) user_role FK    "DEFAULT Member"
        VARCHAR(50) account_status "DEFAULT Active"
        TEXT password "NOT NULL  Min 8 characters = 1 letter uppercase + 1 letter lowercase + 1 digit + 1 special character"
    }


    AUTHOR {
        INTEGER ID PK
        TEXT name NOT NULL
    }


    BOOK {
        VARCHAR(13) ISBN PK
        TEXT title "NOT NULL"
        TEXT publisher "NOT NULL"
        INTEGER edition "NOT NULL Must larger than 0"
        DATE publication_date "NOT NULL"
        TEXT language "NOT NULL"
        INTEGER number_of_copies_available "NOT NULL Must larger than 0"
        TEXT book_cover_image
        TEXT description "NOT NULL"
    }

    BOOK_GENRES {
        VARCHAR(13) ISBN PK,FK
        VARCHAR(50) genre PK,FK
    }

    BOOK_AUTHOR {
        VARCHAR(13) ISBN PK,FK
        INTEGER author_id PK,FK
    }

    BOOK_COPY {
        INTEGER ID PK
        VARCHAR(13) ISBN FK
        TEXT shelf_location "NOT NULL UNIQUE"
        VARCHAR(50) book_status FK "DEFAULT Available"
    }

    RESERVATION {
        INTEGER reservation_id PK
        INTEGER book_id FK
        INTEGER borrower_id FK
        DATE reservation_date "NOT NULL"
        DATE expiration_date "NOT NULL"
        VARCHAR(50) reservation_status FK "DEFAULT Active"
    }

    DEPOSIT {
        INTEGER borrower_id PK,FK
        INTEGER book_id PK,FK
        DATE issue_date "NOT NULL"
        DATE due_date "NOT NULL"
        DATE return_date
        INTEGER overdue_fines "DEFAULT 0"
        VARCHAR(50) renewal_status FK "DEFAULT First-time"
    }

%% Relationship
    USER ||--o{ MEMBERSHIP_TYPE: membership_type
    USER ||--o{ USER_ROLE: user_role

    BOOK_GENRES }o--|| BOOK: genre
    BOOK_GENRES }o--|| GENRE: ISBN

    BOOK_AUTHOR }o--|| BOOK: ISBN
    BOOK_AUTHOR }o--|| AUTHOR: author_id

    BOOK_COPY }o--|| BOOK: ISBN
    BOOK_COPY }o--|| BOOK_STATUS: book_status

    RESERVATION }o--|| BOOK_COPY: book_id
    RESERVATION }o--|| USER: borrower_id

    DEPOSIT }o--|| USER : borrower_id
    DEPOSIT }o--|| BOOK_COPY : book_id
    DEPOSIT }o--|| RENEWAL_STATUS: renewal_status
    RESERVATION }o--|| RESERVATION_STATUS: reservation_status
```
OPTIONS:
* Best Quality Image: [Open this file with Web Browser (Chrome, Edge, Safari) :star:](./mermaid-diagram-2024-08-19-170220.svg)

* PNG Image: [Click here to view the PNG file :framed_picture:](./mermaid-diagram-2024-08-19-170221.png) 