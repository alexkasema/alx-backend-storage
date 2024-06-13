-- A SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
	DECLARE project_id INT;

	-- Check if project exists
	SELECT id INTO project_id FROM projects
	WHERE name = project_name;
	
	-- If project doesn't exists, insert it
	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Insert the correction
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END $$
DELIMITER ; $$
