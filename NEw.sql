create database helloworld;
use helloworld;
create table products (
    ProductID int primary key,
    Name varchar(100),
    Price decimal(10, 2),
    Description text
);
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20)
);
