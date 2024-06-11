# Write your MySQL query statement below
WITH source AS (
    SELECT id,
        num,
        lag(num, 1) over (order by id) as prev_num,
        lag(id, 1) over (order by id) as prev_id,
        lead(num, 1) over (order by id) as next_num,
        lead(id) over (order by id) as next_id
    FROM Logs
)
select distinct(num) as ConsecutiveNums
from source
where num = prev_num
    and num = next_num
    and prev_id = id - 1
    and next_id = id + 1;