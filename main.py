from flask import Flask

app = Flask(__name__)


@app.route('/')
def begin():
    return '通了'


if __name__ == '__main__':
    app.run(port=8080)
