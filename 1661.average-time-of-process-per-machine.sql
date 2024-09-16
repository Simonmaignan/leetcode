-- https://leetcode.com/problems/average-time-of-process-per-machine
SELECT
    machine_id,
    round(cast(avg(process_time) as numeric), 3) as processing_time
FROM(
    SELECT
        machine_id,
        process_id, 
        max(timestamp) - min(timestamp) as process_time
    FROM Activity
    GROUP BY machine_id, process_id
)
GROUP BY machine_id