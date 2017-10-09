HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'pan'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)