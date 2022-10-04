# CONNECTING TO MYSQL WITH GOOGLE COLLAB - PYTHON FRAMEWORK

#######################
##  INSTALL PACKAGES ##
#######################

# !sudo apt-get install python3-dev default-libmysqlclient-dev
# !pip3 install pymysql

# change this to your IP address which is found on your AZURE dashboard
MYSQL_HOSTNAME = ‘XX.XX.XX.XX
MYSQL_USER = 'XXX'
MYSQL_PASSWORD = 'XXXXX'
MYSQL_DATABASE = ‘XXXXX'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print(engine.table_names())

height_weight_data = pd.read_csv(
    '/Users/carolinesanicola/Documents/GitHub/mysql-selfmanaged/data/height_weight_data.csv')
height_weight_data.to_sql('height_weight_data', con=engine, if_exists='append')
