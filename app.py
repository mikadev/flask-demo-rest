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


@app.route('/data')
def all_data():
    return data


@app.route('/data/<int:id>')
def by_id(id):
    return data[id]


if __name__ == '__main__':
    app.run()
