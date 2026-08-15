-- Write your query below
SELECT name from customers LEFT JOIN orders ON orders.customer_id=customers.id WHERE orders.customer_id is NULL;