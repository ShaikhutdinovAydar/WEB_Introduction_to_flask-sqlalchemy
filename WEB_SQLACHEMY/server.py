from flask import Flask
from data import db_session

from WEB_SQLACHEMY.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/ mars_explorer.db")
    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
