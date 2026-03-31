-- View all users
SELECT * FROM users;

-- Count users
SELECT COUNT(*) FROM users;

-- Get specific user
SELECT name, email FROM users WHERE id = 1;

-- Validate no duplicate emails
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Check null values
SELECT * FROM users WHERE email IS NULL;
