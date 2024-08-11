# Sequence Diagrams

Features:
1. <a href="#authentication">Authentication</a>
2. <a href="#common-features">Common Features</a>
3. <a href="#member-only">Member Only :student:</a> 
4. <a href="#librarian-only">Librarian Only :book:</a> 
5. <a href="#admin-only">Admin Only :desktop_computer:</a> 

Actors in **Library Systems Management**:
1. User
2. Client
3. Server
4. Database

## Authentication

Features:
1. <a href="#register">Register</a>
2. <a href="#login">Login</a>
3. <a href="#logout">Logout</a>

### Register
```mermaid
---
    title: Register New User
---
sequenceDiagram
    actor User
    actor Client
    actor Server
    actor Database

    User->>+Client: Click Register Button

    Client->>+Server: Send request to create new account
    Server->>-Client: Redirect to /register

    User->>Client: Input user info (username, password,...)

    Client->>+Server: Send user info (username, password,...)
    Server->>Database: Update info in Database
    Server->>-Client: Redirect to /index + 
    Client->>-User: Show Success Message 
```

### Login 
```mermaid
---
    title: Login 
---
sequenceDiagram
    actor User
    actor Client
    actor Server
    actor Database

    User->>+Client: Click Login Button

    Client->>+Server: Send request to login 
    Server->>-Client: Redirect to /login

    User->>Client: Input user info (username, password,...)

    Client->>+Server: Send user info (username, password,...)
    
    Server->>+Database: Get user with username, password
    Database->>-Server: Send a Record or None

    alt incorrect info
        Server->>Client: Send not correct info
        Client->>User: Show incorrect info message or Create New Account
    else correct info
        Server->>-Client: Redirect to /index page
        Client->>-User: Show Success message 
    end
```

### Logout 
```mermaid
---
    title: Logout
---
sequenceDiagram
    actor User
    actor Client
    actor Server
    actor Database

    User->>+Client: Click Logout Button
    Client->>+Server: Clear User session
    Server->>-Client: Redirect to /index 
    Client->>-User: Show Success Message
```

-------------------------------------------------------------------------------

## Common Features
Features:
1. <a href="#view-all-books">View All Books</a>
2. <a href="#update-user-info">Update Personal Info</a>

### View All Books
```mermaid
---
title: View books
---
sequenceDiagram
    actor User as Member + Librarian + Admin
    actor Client
    actor Server
    actor Database
    
    User->>+Client: Visit the Website URL
    Client->>+Server: Visit /index
    Server->>Client: Redirect to /index

    Server->>+Database: Request all the books
    Database->>-Server: Return all the available books
    Server->>-Client: Send all the available books 

    Client->>-User: Show all the available books
```

### Update User Info
```mermaid
---
    title: Update User Info
---
sequenceDiagram
    actor User as Member + Librarian + Admin
    actor Client
    actor Server
    actor Database

    User->>+Client: Click on Update Info Button
    Client->>+Server: Request to change own user info

    %% Login Required Part
    alt not login yet
        Server->>Client: Redirect to /login Page
        User->>Client: Input user info (username, password)
        Client->>Server: Send user info (username, password)
    end

    %% If Has Login
    Server->>-Client: Redirect to /update_info page
    User->>Client: Update new info and submit

    %% Update info Part
    Client->>+Server: Send new info
    Server->>Database: Update info in Database
    Server->>-Client: Redirect to /update_info with updated info
    
    Client->>User: Show updated info
    Client->>-User: Show Success Message
```

-------------------------------------------------------------------------------

## Member Only
TODO: Implement features that only member can do

## Librarian Only
TODO: Implement features that only librarian can do

## Admin Only
TODO: Implement features that only admin can do