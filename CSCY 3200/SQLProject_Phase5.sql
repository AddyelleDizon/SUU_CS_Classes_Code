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