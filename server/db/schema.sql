-- DROP DATABASE IF EXISTS library_app;
--CREATE DATABASE library_app;

-- Create the format table for book formats, such as paperback and hardback
CREATE TABLE public.format
(
    format_id INT PRIMARY KEY,
    format_type VARCHAR(50)
);

-- Create the book table to store information about the books in the library
CREATE TABLE public.book
(
    book_id INT PRIMARY KEY,
    title VARCHAR(50),
    author VARCHAR(50),
    book_description VARCHAR(250),
    release_date DATE,
    ISBN VARCHAR(17),
    format_id INT,
    FOREIGN KEY (format_id) REFERENCES public.format (format_id)
);

-- Create the table to store book tags such as fantasy, romance, etc
CREATE TABLE tag
(
    tag_id INT PRIMARY KEY,
    tag_name VARCHAR(50)
);

-- Create the book_tags table to link the books and tags together
CREATE TABLE book_tags
(
    tag_id INT,
    book_id INT,
    (tag_id, book_id) PRIMARY KEY,
    FOREIGN KEY (tag_id) REFERENCES public.tag (tag_id)
    FOREIGN KEY (book_id) REFERENCES public.book (book_id)
);

-- Create the user_type table to store user types and permissions
CREATE TABLE user_type
(
    type_id INT PRIMARY KEY,
    type VARCHAR(50),
    type_description VARCHAR(250),
    book_admin BOOLEAN DEFAULT false,
    tag_admin BOOLEAN DEFAULT false,
    user_admin BOOLEAN DEFAULT false,
    status_admin BOOLEAN DEFAULT false
);

-- Create the user table
CREATE TABLE user
(
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    email VARCHAR(250),
    mobile VARCHAR(20),
    postcode VARCHAR(10),
    type_id INT,
    FOREIGN KEY (type_id) REFERENCES public.user_type (type_id)
);

-- Create table to store statuses for books, such as available, borrowed, etc.
CREATE TABLE status
(
    status_id INT PRIMARY KEY,
    status_name VARCHAR(50)
);

-- Create table to link the books with their status and a user (in case the book has been borrowed)
CREATE TABLE book_status
(
    book_id INT,
    status_id INT,
    user_id INT,
    (book_id, status_id, user_id) PRIMARY KEY,
    FOREIGN KEY (book_id) REFERENCES public.book (book_id),
    FOREIGN KEY (status_id) REFERENCES public.status (status_id),
    FOREIGN KEY (user_id) REFERENCES public.user (user_id)
);