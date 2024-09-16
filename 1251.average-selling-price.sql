-- https://leetcode.com/problems/average-selling-price
SELECT 
    p.product_id,
    coalesce(ROUND(SUM(CAST(p.price as numeric) * us.units) / SUM(us.units), 2), 0.00) AS average_price
    -- IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM
    Prices p
    LEFT JOIN UnitsSold us
    ON (p.product_id = us.product_id AND us.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY p.product_id