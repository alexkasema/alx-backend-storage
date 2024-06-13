-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- 	user_id, a users.id value (you can assume user_id is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_weighted_score DECIMAL(10, 2);

	SELECT IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0) INTO avg_weighted_score
	FROM corrections c
		JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	UPDATE users
	SET users.average_score = avg_weighted_score
	WHERE users.id = user_id;

END $$
DELIMITER ; $$
