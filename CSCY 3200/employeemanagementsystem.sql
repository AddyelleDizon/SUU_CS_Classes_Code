-- Drop and recreate database
DROP DATABASE IF EXISTS employeemanagementsystem;
CREATE DATABASE employeemanagementsystem;
USE employeemanagementsystem;

-- Create Employee table
CREATE TABLE Employee (
    employeeID_name VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL,
    number VARCHAR(15) NOT NULL,
    jobTitle VARCHAR(30) NOT NULL,
    department VARCHAR(30) NOT NULL,
    managerID VARCHAR(20) NULL,
    CONSTRAINT PK_Employee PRIMARY KEY (employeeID_name),
    CONSTRAINT FK_Employee_Manager FOREIGN KEY (managerID) REFERENCES Employee(employeeID_name),
    CONSTRAINT CHK_Employee_Phone CHECK (number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'),
    CONSTRAINT CHK_Employee_JobTitle CHECK (jobTitle IN ('Manager', 'Chef', 'Server', 'Host', 'Bartender', 'Dishwasher'))
);

-- Create Payroll table
CREATE TABLE Payroll (
    payrollID INT NOT NULL AUTO_INCREMENT,
    employeeID VARCHAR(20) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    payDate DATE NOT NULL,
    paymentMethod VARCHAR(20) NOT NULL,
    CONSTRAINT PK_Payroll PRIMARY KEY (payrollID),
    CONSTRAINT FK_Payroll_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID_name)
);

-- Create TaxRecord table
CREATE TABLE TaxRecord (
    employeeID VARCHAR(20) NOT NULL,
    taxDeductions DECIMAL(10,2) NOT NULL,
    stateTax DECIMAL(10,2) NOT NULL,
    federalTax DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_TaxRecord PRIMARY KEY (employeeID),
    CONSTRAINT FK_TaxRecord_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID_name)
);

-- Create FinanceRecords table
CREATE TABLE FinanceRecords (
    financeID INT NOT NULL AUTO_INCREMENT,
    employeeID VARCHAR(20) NOT NULL,
    paymentStatus VARCHAR(20) NOT NULL,
    payrollExpenses DECIMAL(12,2) NOT NULL,
    taxExpenses DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_FinanceRecords PRIMARY KEY (financeID),
    CONSTRAINT FK_FinanceRecords_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID_name)
);

-- Create Restaurant table
CREATE TABLE Restaurant (
    restaurantID_name VARCHAR(20) NOT NULL,
    location VARCHAR(100) NOT NULL,
    number VARCHAR(15) NOT NULL,
    managerID VARCHAR(20) NULL,
    CONSTRAINT PK_Restaurant PRIMARY KEY (restaurantID_name),
    CONSTRAINT FK_Restaurant_Employee FOREIGN KEY (managerID) REFERENCES Employee(employeeID_name)
);

-- Create Manager table
CREATE TABLE Manager (
    managerID VARCHAR(20) NOT NULL,
    fName VARCHAR(30) NOT NULL,
    lName VARCHAR(30) NOT NULL,
    restaurantID VARCHAR(20) NOT NULL,
    employeeID VARCHAR(20) NOT NULL,
    department VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Manager PRIMARY KEY (managerID),
    CONSTRAINT FK_Manager_Restaurant FOREIGN KEY (restaurantID) REFERENCES Restaurant(restaurantID_name),
    CONSTRAINT FK_Manager_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID_name)
);

-- Insert Managers first as Employees (with MNGxxx IDs)
INSERT INTO Employee (employeeID_name, address, number, jobTitle, department, managerID)
VALUES 
('MNG001', '123 Cedar City, Utah', '555-123-4567', 'Manager', 'Operations', NULL),
('MNG002', '456 Cedar City, Utah', '555-234-5678', 'Manager', 'Finance', 'MNG001'),
('MNG003', '789 Cedar City, Utah', '555-345-6789', 'Manager', 'HR', 'MNG001'),
('MNG004', '101 Cedar City, Utah', '555-456-7890', 'Manager', 'Kitchen', 'MNG001'),
('MNG005', '111 Cedar City, Utah', '555-567-8901', 'Manager', 'Operations', 'MNG001');

-- Insert regular Employees (reporting to MNGxxx managers)
INSERT INTO Employee (employeeID_name, address, number, jobTitle, department, managerID)
VALUES 
('EMP001', '222 Cedar City, Utah', '555-678-9012', 'Chef', 'Kitchen', 'MNG004'),
('EMP002', '333 Cedar City, Utah', '555-789-0123', 'Server', 'Front', 'MNG002'),
('EMP003', '444 Cedar City, Utah', '555-890-1234', 'Bartender', 'Bar', 'MNG002'),
('EMP004', '555 Cedar City, Utah', '555-901-2345', 'Host', 'Front', 'MNG003'),
('EMP005', '666 Cedar City, Utah', '555-012-3456', 'Dishwasher', 'Kitchen', 'MNG004'),
('EMP006', '777 Cedar City, Utah', '555-123-4567', 'Server', 'Front', 'MNG003'),
('EMP007', '888 Cedar City, Utah', '555-234-5678', 'Chef', 'Kitchen', 'MNG004');

-- Insert Payroll Data
INSERT INTO Payroll (employeeID, salary, payDate, paymentMethod)
VALUES 
('MNG001', 75000.00, '2024-03-01', 'Direct Deposit'),
('MNG002', 65000.00, '2024-03-01', 'Direct Deposit'),
('MNG003', 62000.00, '2024-03-01', 'Direct Deposit'),
('MNG004', 68000.00, '2024-03-01', 'Direct Deposit'),
('MNG005', 60000.00, '2024-03-01', 'Direct Deposit'),
('EMP001', 45000.00, '2024-03-01', 'Check'),
('EMP002', 32000.00, '2024-03-01', 'Cash');

-- Insert Tax Records
INSERT INTO TaxRecord (employeeID, taxDeductions, stateTax, federalTax)
VALUES 
('MNG001', 5000.00, 3000.00, 10000.00),
('MNG002', 4500.00, 2800.00, 9500.00),
('MNG003', 4200.00, 2600.00, 9000.00),
('MNG004', 4800.00, 2900.00, 9800.00),
('MNG005', 4000.00, 2500.00, 8500.00),
('EMP001', 3000.00, 2000.00, 7000.00),
('EMP002', 2500.00, 1500.00, 6000.00);

-- Insert Finance Records
INSERT INTO FinanceRecords (employeeID, paymentStatus, payrollExpenses, taxExpenses)
VALUES 
('MNG001', 'Paid', 75000.00, 13000.00),
('MNG002', 'Pending', 65000.00, 12000.00),
('MNG003', 'Processed', 62000.00, 11500.00),
('MNG004', 'Paid', 68000.00, 12500.00),
('MNG005', 'Pending', 60000.00, 11000.00);

-- Insert Restaurants (initially with NULL managerID)
INSERT INTO Restaurant (restaurantID_name, location, number, managerID)
VALUES 
('Rest001', '135 N college way, Cedar City', '555-111-2222', NULL),
('Rest002', '48 Main Street, Cedar City', '555-222-3333', NULL),
('Rest003', '19 W Henock 30 N, Cedar', '555-333-4444', NULL),
('Rest004', '70 Dr Grey S', '555-444-5555', NULL),
('Rest005', '30 N Beverly Street, Cedar City', '555-555-6666', NULL),
('Rest006', '268 S College Way, Cedar City', '555-666-7777', NULL);

-- Insert Managers into Manager table
INSERT INTO Manager (managerID, fName, lName, restaurantID, employeeID, department)
VALUES 
('MNG001', 'John', 'Smith', 'Rest001', 'MNG001', 'Operations'),
('MNG002', 'Sarah', 'Johnson', 'Rest002', 'MNG002', 'Finance'),
('MNG003', 'David', 'Brown', 'Rest003', 'MNG003', 'HR'),
('MNG004', 'Emily', 'Clark', 'Rest004', 'MNG004', 'Kitchen'),
('MNG005', 'Michael', 'Davis', 'Rest005', 'MNG005', 'Operations');

-- Update Restaurant Managers 
UPDATE Restaurant SET managerID = 'MNG001' WHERE restaurantID_name = 'Rest001';
UPDATE Restaurant SET managerID = 'MNG002' WHERE restaurantID_name = 'Rest002';
UPDATE Restaurant SET managerID = 'MNG003' WHERE restaurantID_name = 'Rest003';
UPDATE Restaurant SET managerID = 'MNG004' WHERE restaurantID_name = 'Rest004';
UPDATE Restaurant SET managerID = 'MNG004' WHERE restaurantID_name = 'Rest004';

-- Show all tables and data
SHOW TABLES;
SELECT * FROM Employee;
SELECT * FROM Payroll;
SELECT * FROM TaxRecord;
SELECT * FROM FinanceRecords;
SELECT * FROM Restaurant;
SELECT * FROM Manager;