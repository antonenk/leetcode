-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

CREATE TEMPORARY TABLE Employee (
    id int,
    name varchar(255),
    department varchar(255),
    managerId int,
    PRIMARY KEY (id)
);

INSERT INTO Employee (id, name, department, managerId) VALUES
    ('101', 'John', 'A', NULL),
    ('102', 'Dan', 'A', '101'),
    ('103', 'James', 'A', '101'),
    ('104', 'Amy', 'A', '101'),
    ('105', 'Anne', 'A', '101'),
    ('106', 'Ron', 'B', '101');

SELECT
    name
FROM
    Employee
WHERE
    id IN (SELECT managerId AS id FROM Employee GROUP BY managerId HAVING COUNT(*)>=5)
