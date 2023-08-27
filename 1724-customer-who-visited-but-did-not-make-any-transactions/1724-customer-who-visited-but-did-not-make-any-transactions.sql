# Write your MySQL query statement below

select v.customer_id, count(v.customer_id) as count_no_trans
from visits v
left join Transactions t
using(visit_id)
where t.transaction_id is NULL
group by v.customer_id
order by count_no_trans DESC