-- creates a stored procedure that computes
-- and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INT
)
BEGIN
	DECLARE avg_score FLOAT;

	-- calculate the average score for the user
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	-- update the average score in the users table
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END //

DELIMITER ;
