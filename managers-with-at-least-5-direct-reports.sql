SELECT
    e.name
FROM
    (SELECT managerId AS id FROM Employee WHERE managerId IS NOT NULL GROUP BY managerId HAVING COUNT(*)>=5) AS m
    LEFT JOIN Employee e ON e.id=m.id
WHERE
    e.id IS NOT NULL
