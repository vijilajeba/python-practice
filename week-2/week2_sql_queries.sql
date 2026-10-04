CREATE DATABASE skillnexius_week2;
use skillnexius_week2;
SELECT COUNT(*) AS total_rows
FROM sales;
select customer_name, sum(total_price) from sales
group by customer_name
order by sum(total_price) desc
limit 10;
select order_id, sum(total_price) as order_total from sales
group by order_id;
select avg(order_total)
from(
      select order_id, sum(total_price) as order_total from sales
       group by order_id
)as order_summary;
	
