-- View for raw metrics per customer
DROP VIEW IF EXISTS vw_customer_metrics;
CREATE VIEW vw_customer_metrics AS
SELECT 
    customer_id,
    SUM(is_success) AS frequency,
    SUM(booking_value) AS monetary_value,
    AVG(booking_value) AS avg_ticket_size
FROM fact_trips
GROUP BY customer_id;

-- View for final CRM Segmentation (The Pivot Logic)
DROP VIEW IF EXISTS vw_customer_segments;
CREATE VIEW vw_customer_segments AS
SELECT 
    customer_id,
    frequency,
    monetary_value,
    CASE 
        WHEN frequency = 3 THEN 'Champion'
        WHEN frequency = 2 THEN 'Loyal'
        WHEN frequency = 1 THEN 'At Risk'
        ELSE 'New/Inactive'
    END AS segment_label
FROM vw_customer_metrics;