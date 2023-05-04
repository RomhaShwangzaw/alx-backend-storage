-- This script creates a stored procedure `ComputeAverageScoreForUser`
-- that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
UPDATE users
SET average_score = (
	SELECT AVG(score)
	FROM corrections AS C
	WHERE C.user_id = user_id
)
WHERE id = user_id;
