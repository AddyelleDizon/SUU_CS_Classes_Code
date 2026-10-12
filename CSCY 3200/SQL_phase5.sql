-- Drop and recreate database
DROP DATABASE IF EXISTS employeemanagementsystem;
CREATE DATABASE employeemanagementsystem;
USE employeemanagementsystem;

-- Create Employee table
CREATE TABLE Employee (
    employeeID VARCHAR(20) NOT NULL,
    fName VARCHAR(30) NOT NULL,
    lName VARCHAR(30) NOT NULL,
    address VARCHAR(100) NOT NULL,
    number VARCHAR(15) NOT NULL,
    jobTitle VARCHAR(30) NOT NULL,
    department VARCHAR(30) NOT NULL,
    managerID VARCHAR(20) NULL,
    CONSTRAINT PK_Employee PRIMARY KEY (employeeID),
    CONSTRAINT FK_Employee_Manager FOREIGN KEY (managerID) REFERENCES Employee(employeeID),
    CONSTRAINT CHK_Employee_Phone CHECK (number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'),
    CONSTRAINT CHK_Employee_JobTitle CHECK (jobTitle IN ('Manager', 'Chef', 'Server', 'Host', 'Bartender', 'Dishwasher'))
);

-- Create Payroll table
CREATE TABLE Payroll (
    payrollID INT NOT NULL AUTO_INCREMENT,
    employeeID VARCHAR(20) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    paymentStartDate DATE NOT NULL,
    paymentMethod VARCHAR(20) NOT NULL,
    CONSTRAINT PK_Payroll PRIMARY KEY (payrollID),
    CONSTRAINT FK_Payroll_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID)
);

-- Create TaxRecord table
CREATE TABLE TaxRecord (
    employeeID VARCHAR(20) NOT NULL,
    taxDeductions DECIMAL(10,2) NOT NULL,
    stateTax DECIMAL(10,2) NOT NULL,
    federalTax DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_TaxRecord PRIMARY KEY (employeeID),
    CONSTRAINT FK_TaxRecord_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID)
);

-- Create FinanceRecords table
CREATE TABLE FinanceRecords (
    financeID INT NOT NULL AUTO_INCREMENT,
    employeeID VARCHAR(20) NOT NULL,
    paymentStatus VARCHAR(20) NOT NULL,
    payrollExpenses DECIMAL(12,2) NOT NULL,
    taxExpenses DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_FinanceRecords PRIMARY KEY (financeID),
    CONSTRAINT FK_FinanceRecords_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID)
);

-- Create Restaurant table
CREATE TABLE Restaurant (
    restaurantID_name VARCHAR(20) NOT NULL,
    location VARCHAR(100) NOT NULL,
    number VARCHAR(15) NOT NULL,
    managerID VARCHAR(20) NULL,
    CONSTRAINT PK_Restaurant PRIMARY KEY (restaurantID_name),
    CONSTRAINT FK_Restaurant_Employee FOREIGN KEY (managerID) REFERENCES Employee(employeeID)
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
    CONSTRAINT FK_Manager_Employee FOREIGN KEY (employeeID) REFERENCES Employee(employeeID)
);

-- Insert Managers first as Employees (with MNGxxx IDs)
INSERT INTO Employee (employeeID, fname, lname, address, number, jobTitle, department, managerID)
VALUES 
('MNG001', 'John', 'Smith', '123 Cedar City, Utah', '555-123-4567', 'Manager', 'Operations', NULL),
('MNG002', 'Sarah', 'Johnson', '456 Cedar City, Utah', '555-234-5678', 'Manager', 'Finance', 'MNG001'),
('MNG003', 'David', 'Brown', '789 Cedar City, Utah', '555-345-6789', 'Manager', 'HR', 'MNG001'),
('MNG004', 'Emily', 'Clark', '101 Cedar City, Utah', '555-456-7890', 'Manager', 'Kitchen', 'MNG001'),
('MNG005', 'Michael', 'Davis', '111 Cedar City, Utah', '555-567-8901', 'Manager', 'Operations', 'MNG001');

-- Insert regular Employees (reporting to MNGxxx managers)
INSERT INTO Employee (employeeID, fname, lname, address, number, jobTitle, department, managerID)
VALUES 
('EMP001', 'Steve', 'Jobs', '222 Cedar City, Utah', '555-678-9012', 'Chef', 'Kitchen', 'MNG004'),
('EMP002', 'Bill', 'Gates', '333 Cedar City, Utah', '555-789-0123', 'Server', 'Front', 'MNG002'),
('EMP003', 'Jeff', 'Bezos', '444 Cedar City, Utah', '555-890-1234', 'Bartender', 'Bar', 'MNG002'),
('EMP004', 'Jensen', 'Huang', '555 Cedar City, Utah', '555-901-2345', 'Host', 'Front', 'MNG003'),
('EMP005', 'Tim', 'Cook', '666 Cedar City, Utah', '555-012-3456', 'Dishwasher', 'Kitchen', 'MNG004'),
('EMP006', 'Mark', 'Zuckerberg', '777 Cedar City, Utah', '555-123-4567', 'Server', 'Front', 'MNG003'),
('EMP007', 'Satya', 'Nadella', '888 Cedar City, Utah', '555-234-5678', 'Chef', 'Kitchen', 'MNG004');

-- Insert Payroll Data
INSERT INTO Payroll (employeeID, salary, paymentStartDate, paymentMethod)
VALUES 
('MNG001', 75000.00, '2020-03-01', 'Direct Deposit'),
('MNG002', 65000.00, '2022-03-01', 'Direct Deposit'),
('MNG003', 62000.00, '2023-03-01', 'Direct Deposit'),
('MNG004', 68000.00, '2021-03-01', 'Direct Deposit'),
('MNG005', 60000.00, '2025-03-01', 'Direct Deposit'),
('EMP001', 45000.00, '2024-03-01', 'Check'),
('EMP002', 32000.00, '2025-03-01', 'Cash'),
('EMP003', 45000.00, '2023-03-01', 'Check'),
('EMP004', 40000.00, '2024-03-01', 'Direct Deposit'),
('EMP005', 40000.00, '2024-03-01', 'Direct Deposit'),
('EMP006', 32000.00, '2025-03-01', 'Cash'),
('EMP007', 50000.00, '2020-03-01', 'Direct Deposit');

-- Insert Tax Records
INSERT INTO TaxRecord (employeeID, taxDeductions, stateTax, federalTax)
VALUES 
('MNG001', 5000.00, 3000.00, 10000.00),
('MNG002', 4500.00, 2800.00, 9500.00),
('MNG003', 4200.00, 2600.00, 9000.00),
('MNG004', 4800.00, 2900.00, 9800.00),
('MNG005', 4000.00, 2500.00, 8500.00),
('EMP001', 3000.00, 2000.00, 7000.00),
('EMP002', 2500.00, 1500.00, 6000.00),
('EMP003', 3000.00, 2000.00, 7000.00),
('EMP004', 2700.00, 1700.00, 6500.00),
('EMP005', 2700.00, 1700.00, 6500.00),
('EMP006', 2500.00, 1500.00, 6000.00),
('EMP007', 3250.00, 2250.00, 7500.00);

-- Insert Finance Records
INSERT INTO FinanceRecords (employeeID, paymentStatus, payrollExpenses, taxExpenses)
VALUES 
('MNG001', 'Late', 65000.00, 13000.00),
('MNG001', 'Paid', 67000.00, 13000.00),
('MNG001', 'Late', 69000.00, 13000.00),
('MNG001', 'Late', 71000.00, 13000.00),
('MNG001', 'Paid', 73000.00, 13000.00),
('MNG001', 'Late', 75000.00, 13000.00),
('MNG002', 'Late', 59000.00, 12000.00),
('MNG002', 'Late', 61000.00, 12000.00),
('MNG002', 'Late', 63000.00, 12000.00),
('MNG002', 'Pending', 65000.00, 12000.00),
('MNG003', 'Paid', 58000.00, 11500.00),
('MNG003', 'Paid', 60000.00, 11500.00),
('MNG003', 'Processed', 62000.00, 11500.00),
('MNG004', 'Late', 60000.00, 12500.00),
('MNG004', 'Paid', 62000.00, 12500.00),
('MNG004', 'Late', 64000.00, 12500.00),
('MNG004', 'Paid', 66000.00, 12500.00),
('MNG004', 'Pending', 68000.00, 12500.00),
('MNG005', 'Processed', 60000.00, 11000.00),
('EMP001', 'Late', 43000.00, 9000.00),
('EMP001', 'Pending', 45000.00, 9000.00),
('EMP002', 'Processed', 32000.00, 7500.00),
('EMP003', 'Paid', 41000.00, 9000.00),
('EMP003', 'Paid', 43000.00, 9000.00),
('EMP003', 'Processed', 45000.00, 9000.00),
('EMP004', 'Late', 38000.00, 8200.00),
('EMP004', 'Pending', 40000.00, 8200.00),
('EMP005', 'Paid', 38000.00, 8200.00),
('EMP005', 'Processed', 40000.00, 8200.00),
('EMP006', 'Late', 32000.00, 7500.00),
('EMP007', 'Late', 40000.00, 9750.00),
('EMP007', 'Late', 42000.00, 9750.00),
('EMP007', 'Paid', 44000.00, 9750.00),
('EMP007', 'Late', 46000.00, 9750.00),
('EMP007', 'Paid', 48000.00, 9750.00),
('EMP007', 'Pending', 50000.00, 9750.00);

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

-- Calculate total payroll expenses for the last 2 years
SELECT SUM(COALESCE(salary, 0) + COALESCE(taxExpenses, 0)) AS total_payroll_expense
FROM Payroll
JOIN FinanceRecords ON Payroll.employeeID = FinanceRecords.employeeID
WHERE paymentStartDate >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR);

-- Find all employees who worked for more than a year and their current salary
SELECT e.employeeID, e.fname, e.lname, p.salary AS new_salary
FROM Employee e
JOIN Payroll p ON e.employeeID = p.employeeID
WHERE e.employeeID IN (
    SELECT employeeID
    FROM Payroll
    WHERE paymentStartDate <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
);

-- Find all employees with 2 or more late payments
SELECT e.employeeID, e.fname, e.lname, COUNT(f.paymentStatus) AS late_payments
FROM Employee e
JOIN FinanceRecords f ON e.employeeID = f.employeeID
WHERE f.paymentStatus = 'Late'
GROUP BY e.employeeID
HAVING COUNT(f.paymentStatus) >= 2;

-- Calculate percentage of payroll expenses attributed to tax deducations
SELECT 
    SUM(t.taxDeductions + t.stateTax + t.federalTax) / SUM(f.payrollExpenses) * 100 AS tax_percentage
FROM TaxRecord t
JOIN FinanceRecords f ON t.employeeID = f.employeeID;

-- Calculate average salary per department
SELECT e.department, COUNT(e.employeeID) AS num_employees, AVG(p.salary) AS avg_salary
FROM Employee e
JOIN Payroll p ON e.employeeID = p.employeeID
GROUP BY e.department
ORDER BY avg_salary DESC;