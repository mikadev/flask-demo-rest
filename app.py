import json

from flask import Flask

app = Flask(__name__)

data = [
    {
        "a": 1
    },
    {
        "b": 2
    }
]

from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rest'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL()
mysql.init_app(app)


# Required


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT* FROM users''')
    rv = cur.fetchall()
    return json.dumps(rv)


@app.route('/data')
def all_data():
    return data


@app.route('/data/<int:id>')
def by_id(id):
    return data[id]


if __name__ == '__main__':
    app.run(debug=True)
