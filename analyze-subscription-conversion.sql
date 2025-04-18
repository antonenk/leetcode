CREATE TABLE if not exists UserActivity (
    user_id INT,
    activity_date DATE,
    activity_type VARCHAR(20),
    activity_duration INT
);
Truncate table UserActivity;
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-01', 'free_trial', '45');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-02', 'free_trial', '30');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-05', 'free_trial', '60');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-10', 'paid', '75');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-12', 'paid', '90');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('1', '2023-01-15', 'paid', '65');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('2', '2023-02-01', 'free_trial', '55');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('2', '2023-02-03', 'free_trial', '25');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('2', '2023-02-07', 'free_trial', '50');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('2', '2023-02-10', 'cancelled', '0');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-05', 'free_trial', '70');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-06', 'free_trial', '60');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-08', 'free_trial', '80');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-12', 'paid', '50');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-15', 'paid', '55');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('3', '2023-03-20', 'paid', '85');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('4', '2023-04-01', 'free_trial', '40');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('4', '2023-04-03', 'free_trial', '35');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('4', '2023-04-05', 'paid', '45');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration) values ('4', '2023-04-07', 'cancelled', '0');


-- beats 21% runtime

SELECT
    user_id,
    ROUND(SUM(IF(activity_type='free_trial',activity_duration,0)) / SUM(IF(activity_type='free_trial',1,0)), 2) AS trial_avg_duration,
    ROUND(SUM(IF(activity_type='paid',      activity_duration,0)) / SUM(IF(activity_type='paid',      1,0)), 2) AS paid_avg_duration
FROM
    UserActivity
GROUP BY
    user_id
HAVING
    paid_avg_duration IS NOT NULL
ORDER BY
    user_id