# Write your MySQL query statement below
WITH cte AS (
    SELECT *,
        ROW_NUMBER() OVER() AS rn,
        id - ROW_NUMBER() OVER() AS id_diff
    FROM stadium
    WHERE people > 99
)

SELECT id,
    visit_date,
    people
FROM cte
where id_diff IN (
    SELECT id_diff
    FROM cte
    GROUP BY id_diff
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;