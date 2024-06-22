-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.

-- The result format is in the following example.

SELECT 
    DISTINCT m.name
FROM employee e
LEFT JOIN employee m ON e.managerId = m.id
WHERE m.id IS NOT NULL
GROUP BY m.name
HAVING COUNT(*) >= 5