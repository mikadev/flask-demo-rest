from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rest'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL()
mysql.init_app(app)
