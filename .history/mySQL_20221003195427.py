# CONNECTING TO MYSQL WITH GOOGLE COLLAB - PYTHON FRAMEWORK

#######################
##  INSTALL PACKAGES ##
#######################

# !sudo apt-get install python3-dev default-libmysqlclient-dev
# !pip3 install pymysql

from sqlalchemy import create_engine

MYSQL_HOSTNAME = 'INSERT_HERE'
MYSQL_USER = 'INSERT_HERE'
MYSQL_PASSWORD = 'INSERT_HERE'
MYSQL_DATABASE = 'INSERT_HERE'

connection_string = f'mysql+pymysql://{MYSQL_USER'