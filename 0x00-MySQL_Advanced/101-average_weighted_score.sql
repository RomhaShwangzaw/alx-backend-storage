-- This script creates a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
UPDATE users AS U,
(SELECT U.id, SUM(C.score * P.weight) / SUM(P.weight) AS w_avg
FROM users AS U
JOIN corrections AS C ON U.id = C.user_id
JOIN projects AS P ON C.project_id = P.id
GROUP BY U.id)
AS WA
SET U.average_score = WA.w_avg
WHERE U.id = WA.id;
