-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions
SELECT customer_id, count(v.visit_id) AS count_no_trans
FROM Visits v LEFT JOIN Transactions t ON v.visit_id=t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id