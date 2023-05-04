-- This script creates a trigger that resets the attribute
-- `valid_email` only when the `email` has been changed.
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email
		THEN
		IF OLD.valid_email = 0
			THEN
			SET NEW.valid_email = 1;
		ELSE
			SET NEW.valid_email = 0;
		END IF;
	END IF;
END
$$
DELIMITER ;