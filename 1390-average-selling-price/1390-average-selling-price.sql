# Write your MySQL query statement below

select p.product_id, round(sum(p.price*u.units)/sum(u.units),2) as average_price
from Prices p
left join UnitsSold u
using(product_id)
where u.purchase_date between p.start_date and p.end_date
group by p.product_id