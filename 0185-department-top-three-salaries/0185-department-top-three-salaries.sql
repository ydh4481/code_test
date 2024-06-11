# Write your MySQL query statement below
WITH rank_salary AS (
    SELECT departmentId,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk
    FROM employee
),

top3 AS (
    SELECT DISTINCT departmentId,
        salary
    FROM rank_salary
    WHERE rk <= 3
)

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.Salary
FROM employee e
JOIN top3 ON e.departmentId=top3.departmentId
    AND e.salary=top3.salary
LEFT JOIN department d ON e.departmentId=d.id;