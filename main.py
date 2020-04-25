from flask import Flask, render_template

from models.news import News
from models import db_session

app = Flask(__name__)
db_session.global_init('sqlite.db')


@app.route('/')
def index():
    session = db_session.create_session()
    return render_template(
        'base.html',
        news=session.query(News).order_by(News.date.desc())
    )


if __name__ == '__main__':
    app.run('127.0.0.1', 8000, True)
