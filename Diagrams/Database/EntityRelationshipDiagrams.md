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
    USER {
        INT ID         PK
        TEXT name
        TEXT address
        TEXT phone_number
        TEXT email_address
        VARCHAR(10) membership_type     FK      "Student || Faculty || Public"  
        VARCHAR(10) user_role           FK      "Admin || Librarian || Member"
        VARCHAR(10) account_status       "Active || Inactive"
        TEXT password
    }

    AUTHOR {
        INT ID         PK
        TEXT name 
    }

    BOOK {
        TEXT ISBN                       PK            "UNIQUE"
        TEXT title
        TEXT publisher
        TEXT edition
        DATE publication_date
        TEXT language
        INT number_of_copies_available
        TEXT book_cover_image "HTTPS URL"
        TEXT description
    }

    BOOK_GENRES {
        TEXT ISBN       PK, FK
        TEXT genre      PK,FK
    }

    BOOK_AUTHOR {
        TEXT ISBN       PK, FK
        INT author_id      PK, FK
    }
    
    BOOK_COPY {
        INT ID     PK
        TEXT ISBN   FK
        TEXT shelf_location             "UNIQUE"
        OPTION book_status      FK      "Available || Borrowed || Reserved"
    }

    RESERVATION {
        INT reservation_id     PK
        INT book_id            FK
        INT borrower_id        FK
        DATE reservation_date   
        DATE expiration_date
        OPTION reservation_status   FK  "Active || Cancelled || Fulfilled"
    }

    DEPOSIT {
        INT borrower_id PK, FK
        INT book_id    PK, FK
        DATE issue_date
        DATE due_date
        DATE return_date
        INT overdue_fines
        OPTION renewal_status    FK   "First-time || Renewed"                
    }

    GENRE {
        VARCHAR(10) genre   PK
        TEXT description
    }

%% Info Table
    MEMBERSHIP_TYPE {
        %% Available Type: "Student || Faculty || Public"
        VARCHAR(10) type    PK
        TEXT description
    }

    USER_ROLE {
        %% Available role: "Admin || Librarian || Member"
        VARCHAR(10) role    PK
        TEXT description
    }

    BOOK_STATUS {
        %% Available status: "Available || Borrowed || Reserved"
        VARCHAR(10) status  PK
        TEXT description
    }

    RESERVATION_STATUS {
        %% Available status: "Active || Cancelled || Fulfilled"
        VARCHAR(10) status  PK
        TEXT description
    }

    RENEWAL_STATUS {
        %% Available status:    "First-time || Renewed"  
        VARCHAR(10) status PK
        TEXT description
    }

%% Relationship
    BOOK_COPY ||--o{ DEPOSIT: book_id
    BOOK_COPY ||--o| RESERVATION: book_id
    BOOK_COPY }|--|| BOOK_STATUS: book_status
    AUTHOR ||--|{ BOOK_AUTHOR: author_id

    BOOK ||--|{ BOOK_COPY: ISBN
    BOOK ||--|{ BOOK_AUTHOR: ISBN
    BOOK ||--|{ BOOK_GENRES: ISBN

    GENRE ||--|{ BOOK_GENRES: genre

    USER ||--o{ DEPOSIT: borrower_id
    USER ||--o{ RESERVATION: borrower_id
    USER }|--|| MEMBERSHIP_TYPE: membership_type
    USER }|--|| USER_ROLE: user_role

    RESERVATION }o--|| RESERVATION_STATUS: reservation_status

    DEPOSIT }o--|| RENEWAL_STATUS: renewal_status
```
OPTIONS:
* Best Quality Image: [Open this file with Web Browser (Chrome, Edge, Safari) :star:](./mermaid-diagram-2024-08-13-221525.svg)

* PNG Image: [Click here to view the PNG file :framed_picture:](./mermaid-diagram-2024-08-13-221526.png) 