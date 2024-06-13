CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
)

-- SELECT * FROM users

-- INSERT INTO users (username, password) VALUES (?, ?)

-- DELETE FROM users WHERE id = ?