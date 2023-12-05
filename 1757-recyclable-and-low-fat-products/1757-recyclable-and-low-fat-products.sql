# Write your MySQL query statement below
SELECT product_id
FROM Products T
WHERE T.low_fats like 'Y' AND T.recyclable  like 'Y';