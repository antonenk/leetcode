-- https://leetcode.com/problems/capital-gainloss/description/
-- beats 39% runtime

Create TEMPORARY Table Stocks (
    stock_name varchar(15),
    operation ENUM('Sell', 'Buy'),
    operation_day int,
    price int
);

insert into Stocks (stock_name, operation, operation_day, price) values 
    ('Leetcode',     'Buy',  1,  1000),
    ('Corona Masks', 'Buy',  2,  10),
    ('Leetcode',     'Sell', 5,  9000),
    ('Handbags',     'Buy',  17, 30000),
    ('Corona Masks', 'Sell', 3,  1010),
    ('Corona Masks', 'Buy',  4,  1000),
    ('Corona Masks', 'Sell', 5,  500),
    ('Corona Masks', 'Buy',  6,  1000),
    ('Handbags',     'Sell', 29, 7000),
    ('Corona Masks', 'Sell', 10, 10000);

SELECT
    stock_name,
    SUM(IF(operation='Buy',-1,1)*price) AS capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name

