# Write your MySQL query statement below
SELECT e.name AS Employee
FROM employee e
LEFT JOIN employee m on e.managerId=m.id
WHERE e.salary > m.salary