# Write your MySQL query statement below
-- Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
-- For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
-- For Pandas users, please note that you are supposed to modify Person in place.
-- After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
-- The result format is in the following example.

WITH row_num AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM person
)
DELETE FROM person
WHERE id IN (
    SELECT id
    FROM row_num
    WHERE rn != 1
)