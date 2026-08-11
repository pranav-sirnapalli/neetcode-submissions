-- Write your query below
select a.name
from customers a
LEFT JOIN orders b
on a.id = b.customer_id
where b.customer_id is NULL