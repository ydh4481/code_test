# Write your MySQL query statement below
-- Write a solution to find all customers who never order anything.
-- Return the result table in any order.
-- The result format is in the following example.

SELECT name AS Customers
FROM customers
WHERE id NOT IN (
    SELECT DISTINCT customerId
    FROM orders
)