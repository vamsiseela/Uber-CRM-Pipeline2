-- 1. Get the final counts for the Report and PPT
SELECT 
    segment_label, 
    COUNT(*) AS total_users, 
    ROUND(SUM(monetary_value), 2) AS total_revenue
FROM vw_customer_segments
GROUP BY segment_label
ORDER BY total_revenue DESC;

-- 2. Diagnostic query to check Rush Hour impact on success
SELECT 
    t.is_rush_hour, 
    AVG(f.is_success) * 100 AS success_rate_percentage
FROM fact_trips f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.is_rush_hour;