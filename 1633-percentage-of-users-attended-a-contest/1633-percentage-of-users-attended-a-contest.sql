# Write your MySQL query statement below
WITH TotalUsers AS (
    SELECT COUNT(DISTINCT user_id) AS total_users
    FROM Users
),
CountRegistrations AS (
SELECT contest_id, COUNT(DISTINCT user_id) AS registered_users
    FROM Register
    GROUP BY contest_id
)
SELECT cr.contest_id, ROUND((cr.registered_users * 100)/tu.total_users, 2) as percentage
FROM totalUsers tu, 
CountRegistrations cr
ORDER BY percentage DESC, cr.contest_id ;