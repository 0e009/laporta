1. check if pdo support is installed 
$php -i|grep PDO
output : 
PDO
PDO support => enabled
PDO drivers => mysql
PDO Driver for MySQL => enabled

if installed ouptut is like above else 
$sudo apt-get install php5-mysql;
