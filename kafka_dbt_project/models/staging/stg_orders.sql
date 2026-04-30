{{ config(materialized='view') }}

select
    product_id,
    revenue,
    order_count,
    window.start as window_start,
    window.end as window_end
from {{ source('default', 'gold_revenue') }}