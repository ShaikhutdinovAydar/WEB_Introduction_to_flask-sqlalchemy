from flask import Flask, render_template
from data import db_session

from WEB_SQLACHEMY.data.db_session import global_init, create_session
from WEB_SQLACHEMY.data.jobs import Jobs
from WEB_SQLACHEMY.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def g():
    global_init(f"db/mars_explorer.db")
    session = create_session()
    listt = []
    for user in session.query(Jobs):
        listt.append(user)
    return render_template('index.html', listt=listt)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
