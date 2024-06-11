# Write your MySQL query statement below
WITH highest_salary AS (
    SELECT departmentId,
        MAX(salary) AS max_salary
    FROM employee
    GROUP BY departmentId
)

SELECT d.name AS Department,
    e.name AS Employee,
    e.Salary
FROM employee e
JOIN highest_salary hs ON e.departmentId=hs.departmentId
    AND e.salary=hs.max_salary
LEFT JOIN department d ON e.departmentId=d.id;