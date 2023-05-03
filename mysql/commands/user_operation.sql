-- create user

-- CREATE USER 'username'@'hostname(ip/computer name)' IDENTIFIED BY 'password';

CREATE USER 'AIoTLab-MySQL'@'102-Router' IDENTIFIED BY 'db309-1';

CREATE USER 'AIoTLab-MySQL'@'%' IDENTIFIED BY 'db309-1';

-- '%' means allow all host(允許網際網路上任意裝置登入)

-- grant all permissions

GRANT ALL PRIVILEGES ON *.* TO 'AIoTLab-MySQL'@'%';

-- list all user

SELECT User, Host FROM mysql.user;

-- in root

-- ALTER USER 'user-name'@'localhost' IDENTIFIED BY 'NEW_USER_PASSWORD';

ALTER USER 'AIoTLab-MySQL'@'102-Router' IDENTIFIED BY 'db309-1';

-- delete user

-- DROP USER 'username'@'hostname'

DROP USER 'AIoTLab-MySQL'@'102-Router';