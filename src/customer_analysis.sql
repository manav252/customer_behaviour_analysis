/* =========================
   Q1. Total Revenue
   ========================= */
SELECT SUM(purchase_amount) AS total_revenue
FROM customer;


/* =========================
   Q2. Average Purchase Amount
   ========================= */
SELECT ROUND(AVG(purchase_amount)::numeric, 2) AS avg_purchase
FROM customer;


/* =========================
   Q3. Total Customers
   ========================= */
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM customer;


/* =========================
   Q4. Revenue by Category
   ========================= */
SELECT category,
SUM(purchase_amount) AS total_revenue
FROM customer
GROUP BY category
ORDER BY total_revenue DESC;


/* =========================
   Q5. Subscription vs Spending
   ========================= */
SELECT subscription_status,
COUNT(customer_id) AS total_customers,
ROUND(AVG(purchase_amount)::numeric, 2) AS avg_spend,
ROUND(SUM(purchase_amount)::numeric, 2) AS total_revenue
FROM customer
GROUP BY subscription_status
ORDER BY total_revenue DESC;


/* =========================
   Q6. Discount Rate by Product
   ========================= */
SELECT item_purchased,
ROUND(
    SUM(CASE WHEN discount_applied = 'Yes' THEN 1 ELSE 0 END)::numeric 
    / COUNT(*), 
2) AS discount_rate
FROM customer
GROUP BY item_purchased
ORDER BY discount_rate DESC
LIMIT 5;


/* =========================
   Q7. Customer Segmentation
   ========================= */
WITH customer_type AS (
    SELECT customer_id, previous_purchases,
    CASE
        WHEN previous_purchases = 1 THEN 'New'
        WHEN previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
        ELSE 'Loyal'
    END AS customer_segment
    FROM customer
)

SELECT customer_segment, COUNT(*) AS total_customers
FROM customer_type
GROUP BY customer_segment
ORDER BY total_customers DESC;


/* =========================
   Q8. Top 3 Products per Category
   ========================= */
WITH item_counts AS (
    SELECT category,
           item_purchased,
           COUNT(customer_id) AS total_orders,
           ROW_NUMBER() OVER (
               PARTITION BY category 
               ORDER BY COUNT(customer_id) DESC
           ) AS item_rank
    FROM customer
    GROUP BY category, item_purchased
)

SELECT category, item_purchased, total_orders
FROM item_counts
WHERE item_rank <= 3
ORDER BY category, item_rank;


/* =========================
   Q9. Repeat Buyers vs Subscription
   ========================= */
SELECT subscription_status,
COUNT(customer_id) AS repeat_buyers
FROM customer
WHERE previous_purchases > 5
GROUP BY subscription_status
ORDER BY repeat_buyers DESC;


/* =========================
   Q10. Revenue by Age Group
   ========================= */
SELECT age_group,
SUM(purchase_amount) AS total_revenue
FROM customer
GROUP BY age_group
ORDER BY total_revenue DESC;