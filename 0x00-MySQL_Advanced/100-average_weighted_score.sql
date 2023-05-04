-- This script creates a stored procedure `ComputeAverageWeightedScoreForUser`
-- that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
UPDATE users
SET average_score = (
	SELECT SUM(C.score * P.weight) / SUM(P.weight)
	FROM corrections AS C
	JOIN projects AS P
	ON C.project_id = P.id
	WHERE C.user_id = user_id
)
WHERE id = user_id;
