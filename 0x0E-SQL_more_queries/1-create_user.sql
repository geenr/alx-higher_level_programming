-- create a user and give the user all prvileges using GRANT ALL PRIVILEGES
-- ensure the password of user is set to user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
