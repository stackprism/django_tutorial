#Todo seperate out into two files, one with and awk script to parse the details from the second file
sudo apt-get -y install debconf-utils
echo "mysql-server-5.5 mysql-server/root_password password $MYSQL_ROOT_PWD" > mysql.preseed
echo "mysql-server-5.5 mysql-server/root_password_again password $MYSQL_ROOT_PWD" >> mysql.preseed
echo "mysql-server-5.5 mysql-server/start_on_boot boolean true" >> mysql.preseed
cat mysql.preseed | sudo debconf-set-selections

