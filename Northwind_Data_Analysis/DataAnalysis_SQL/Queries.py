# 1. Show all products ordered by one customer

customer_wise_order_detail = """SELECT CST.first_name, CST.last_name, CST.job_title, CST.city, CST.state_province, 
ORD.id, ORD.order_date, ORD.ship_name, ORD.ship_city,
ODT.product_id, ODT.quantity, ODT.unit_price, PRD.product_code, PRD.product_name FROM northwind.orders AS ORD
INNER JOIN northwind.customers AS CST
ON ORD.customer_id=CST.id
INNER JOIN northwind.order_details AS ODT
ON ORD.id=ODT.order_id
INNER JOIN northwind.products AS PRD
ON ODT.product_id=PRD.id
WHERE CST.id={}"""

# 2. Find highest number orderd product

highest_ordered_product="""SELECT ODT.product_id, SUM(ODT.quantity) AS total_quantity, PRD.product_name  FROM northwind.order_details AS ODT 
INNER JOIN northwind.products AS PRD
ON ODT.product_id=PRD.id
GROUP BY ODT.product_id 
ORDER BY total_quantity DESC LIMIT 1"""

# 3. find top 5 customers who ordered most
 
top_5_customer_who_order_most = """SELECT COUNT(ORD.id) AS num_order , ORD.customer_id, CST.first_name,CST.last_name
FROM northwind.orders AS ORD
INNER JOIN northwind.customers AS CST
ON ORD.customer_id=CST.id
GROUP BY ORD.customer_id
ORDER BY num_order DESC LIMIT 5"""

# 4. Year and month wise highest selling product

highest_selling_product = """SELECT ORD.id AS order_id, ORD.order_date, ODT.product_id, ODT.quantity, ODT.unit_price, PRD.product_name FROM northwind.orders AS ORD
INNER JOIN northwind.order_details ODT
ON ORD.id=ODT.order_id 
INNER JOIN northwind.products AS PRD
ON ODT.product_id=PRD.id"""


# 6. Highest selled product in june 2006

month_wise_highest_sell_product = """SELECT * FROM (SELECT DATE_FORMAT(ORD.order_date,'%Y') AS Y1, DATE_FORMAT(ORD.order_date,'%m') AS M1, PDT.product_name ,SUM(ODT.quantity) AS total_quantity,
SUM(ODT.quantity*ODT.unit_price) AS total_price,
ROW_NUMBER() OVER(PARTITION BY DATE_FORMAT(ORD.order_date,'%m') ORDER BY SUM(ODT.quantity) DESC) AS row_num  
FROM northwind.orders AS ORD
JOIN  northwind.order_details AS ODT
ON ODT.order_id= ORD.id
JOIN northwind.products AS PDT
ON ODT.product_id=PDT.id
-- -- WHERE DATE_FORMAT(ORD.order_date,'%m')='06'
GROUP BY  DATE_FORMAT(ORD.order_date,'%Y'), DATE_FORMAT(ORD.order_date,'%m'), PDT.product_name 
ORDER BY M1,total_quantity DESC ) AS S1 WHERE S1.row_num=1"""

#-- 7. Find highest SELLING product catagory wise
highest_selling_product_catagorywise="""SELECT * FROM(SELECT PRD.category,PRD.product_name, COUNT(ODT.order_id) AS num_of_orders, SUM(ODT.quantity) AS total_quantity, 
SUM(ODT.unit_price* ODT.quantity) AS total_selling_price,  
ROW_NUMBER() OVER (PARTITION BY PRD.category ORDER BY COUNT(ODT.order_id) DESC ) AS row_num
FROM northwind.order_details AS ODT
JOIN northwind.products AS PRD
ON PRD.id=ODT.product_id
GROUP BY PRD.category,PRD.product_name 
ORDER BY PRD.category, num_of_orders DESC, total_selling_price) AS S1 WHERE row_num=1"""

# -- 9. Find product wise monthly sells
product_wise_monthly_sell="""SELECT  DATE_FORMAT(ORD.order_date,'%m') AS month_num, PRD.product_name, 
SUM(ODT.quantity) AS total_quantity,  SUM(ODT.quantity * ODT.unit_price) AS total_price
FROM northwind.order_details AS ODT
JOIN northwind.orders AS ORD
ON ORD.id=ODT.order_id
JOIN northwind.products AS PRD
ON PRD.id=ODT.product_id
GROUP BY  month_num,PRD.product_name
ORDER BY month_num ASC ,PRD.product_name DESC"""

# -- 10. catagory wise monthly sells
catagory_wise_monthly_sell="""SELECT PRD.category,DATE_FORMAT(ORD.order_date, '%m') AS month_num, SUM(ODT.quantity), SUM(ODT.unit_price *ODT.quantity) AS total_price
FROM northwind.products AS PRD
JOIN northwind.order_details AS ODT
ON ODT.product_id=PRD.id
JOIN northwind.orders AS ORD
ON ORD.id=ODT.order_id
GROUP BY PRD.category, month_num"""

