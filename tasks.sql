USE mydb;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT false
);
