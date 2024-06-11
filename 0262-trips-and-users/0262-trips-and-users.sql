# Write your MySQL query statement below
WITH calculate AS (
    SELECT request_at,
        COUNT(*) AS total_cnt,
        SUM(IF(status LIKE 'cancelled%', 1, 0)) AS cancelled_cnt
    FROM trips
    WHERE client_id IN (
            SELECT users_id
            FROM users
            WHERE banned = 'No' AND role = 'client'
        )
        AND driver_id IN (
            SELECT users_id
            FROM users
            WHERE banned = 'No' AND role = 'driver'
        )
    GROUP BY request_at
)
SELECT 
    request_at AS Day,
    ROUND(cancelled_cnt / total_cnt, 2) AS 'Cancellation Rate'
FROM calculate
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03';