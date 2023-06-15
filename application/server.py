from flask import jsonify

from application import app, mysql

data = [
    {
        "a": 1
    },
    {
        "b": 2
    }
]

# Required

"""
[
    {
        "email": "test@mail.fr",
        "id": 1,
        [ 
            {
                "tel": "1010101",
                "ud.id": 1,
                "user_id": 1
            }, 
             {
                "tel": "00220020",
                "ud.id": 1,
                "user_id": 1
            }, 
        ]
    }
]
"""


def compute(a, b):
    return a + b


@app.route('/')
@app.route('/users')
def all_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users u JOIN user_data ud ON u.id = ud.user_id''')
    return jsonify(list(users(cur.fetchall()).values()))


def users(users: dict) -> dict:
    res = {}
    for idx, user in enumerate(users):
        email = user['email']
        tel = user['tel']
        if email in res:
            res[email]['user_data'].append(tel)
        else:
            res[email] = {'email': email, 'user_data': [tel]}
    return res


@app.route('/data')
def all_data():
    return data


@app.route('/data/<int:id>')
def by_id(id):
    return data[id]


if __name__ == '__main__':
    app.run(debug=True)
