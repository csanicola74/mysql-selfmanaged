# mysql-selfmanaged

2022hha507Fall

### when in VM:
#### sudo apt-get update
#### sudo apt install mysql-server mysql-client # installing mysql server and mysql client
#### sudo mysql # logging in
#### show databases; # will show what databases are within the server
#### CREATE USER 'dba'@'%' IDENTIFIED BY 'ahi2022'; # creates a user within the server (the identified by is the password)
#### select user from mysql.user # pulls up the list of users to verify the user was created sucessfully
#### GRANT ALL PRIVILEGES ON *.* TO 'dba'@;%; WITH GRANT OPTION; # give the user you just created privileges to everything
#### show grants for dba; # shows what grant privileges were given to the user to confirm it was done correctly

#### so now you can test the connection by logging in as '$ mysql -u dba -p' and enter the password: ahi2022 and now you can connect in
#### create database tempdata;
select * from mysql.user \G