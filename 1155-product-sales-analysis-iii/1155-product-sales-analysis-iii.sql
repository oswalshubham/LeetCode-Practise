# Write your MySQL query statement below
select product_id, year as first_year, quantity,price
from Sales s
where (s.product_id, s.year) in
(select product_id, min(year)
from sales
group by product_id)