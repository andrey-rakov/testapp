from .db_session import SqlAlchemyBase
from datetime import date
import sqlalchemy as sa


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    content = sa.Column(sa.String)
    date = sa.Column(sa.Date, default=date.today())

    def formated_date(self):
        return self.date.strftime('%d.%m.%Y')
