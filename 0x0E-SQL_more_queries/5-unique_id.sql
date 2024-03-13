-- creates a table whose id is set to a DEFAULT OF 1 and is unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
