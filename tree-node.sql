Create table If Not Exists Tree (id int, p_id int);
Truncate table Tree;
insert into Tree (id, p_id) values ('1', NULL);
insert into Tree (id, p_id) values ('2', '1');
insert into Tree (id, p_id) values ('3', '1');
insert into Tree (id, p_id) values ('4', '2');
insert into Tree (id, p_id) values ('5', '2');


-- beats 69% runtime

SELECT
    n.id,
    IF(
        n.p_id IS NULL,
        'Root',
        IF(c.cnt > 0, 'Inner', 'Leaf')
    )
FROM
    Tree AS n
    LEFT JOIN (SELECT p_id, COUNT(*) AS cnt FROM Tree GROUP BY p_id) AS c ON c.p_id=n.id