# Write your MySQL query statement below
-- Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

WITH add_lag AS (
    SELECT *,
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS prev_temperature
    FROM weather
)

SELECT id
FROM add_lag
WHERE temperature > prev_temperature