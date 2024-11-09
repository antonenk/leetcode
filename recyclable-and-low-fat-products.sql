Create TEMPORARY table Products (
    product_id int,
    low_fats ENUM('Y', 'N'),
    recyclable ENUM('Y','N'),
    PRIMARY KEY (product_id)
);

insert into Products (product_id, low_fats, recyclable) values
('0', 'Y', 'N'),
('1', 'Y', 'Y'),
('2', 'N', 'Y'),
('3', 'Y', 'Y'),
('4', 'N', 'N');

SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable='Y';
