{{ config(
    materialized='incremental',
    unique_key='product_id || window_start'
) }}

select
    product_id,
    window_start,
    window_end,
    revenue,
    order_count,
    revenue / order_count as avg_order_value

from {{ ref('stg_orders') }}

{% if is_incremental() %}
where window_start > (select max(window_start) from {{ this }})
{% endif %}