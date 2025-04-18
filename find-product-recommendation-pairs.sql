CREATE TABLE if not exists ProductPurchases (
    user_id INT,
    product_id INT,
    quantity INT
)
CREATE TABLE  if not exists ProductInfo (
    product_id INT,
    category VARCHAR(100),
    price DECIMAL(10, 2)
)
Truncate table ProductPurchases
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '101', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '102', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '103', '3')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '101', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '102', '5')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '104', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '101', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '103', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '105', '4')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '101', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '102', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '103', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '104', '3')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '102', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '104', '1')

Truncate table ProductInfo
insert into ProductInfo (product_id, category, price) values ('101', 'Electronics', '100')
insert into ProductInfo (product_id, category, price) values ('102', 'Books', '20')
insert into ProductInfo (product_id, category, price) values ('103', 'Clothing', '35')
insert into ProductInfo (product_id, category, price) values ('104', 'Kitchen', '50')
insert into ProductInfo (product_id, category, price) values ('105', 'Sports', '75')

-- beats 100% runtime

SELECT
    p1.product_id AS product1_id,
    p2.product_id AS product2_id,
    i1.category AS product1_category,
    i2.category AS product2_category,
    COUNT(DISTINCT p1.user_id) AS customer_count
FROM
    ProductPurchases p1
    LEFT JOIN ProductPurchases p2 ON p1.user_id=p2.user_id AND p1.product_id < p2.product_id
    LEFT JOIN ProductInfo i1 ON i1.product_id = p1.product_id
    LEFT JOIN ProductInfo i2 ON i2.product_id = p2.product_id
WHERE
    p2.product_id IS NOT NULL
GROUP BY
    p1.product_id,
    p2.product_id
HAVING
    customer_count > 2
ORDER BY
    customer_count DESC,
    p1.product_id,
    p2.product_id

