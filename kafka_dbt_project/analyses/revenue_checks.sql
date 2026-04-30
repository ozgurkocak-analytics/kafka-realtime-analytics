-- Top 5
select product_id, sum(revenue) as total_revenue
from {{ ref('fct_revenue') }}
group by product_id
order by total_revenue desc
limit 5;

-- Anomalies
select *
from {{ ref('fct_revenue') }}
where order_count = 0;