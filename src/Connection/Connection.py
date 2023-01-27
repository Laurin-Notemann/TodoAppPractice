import sqlalchemy as db_orm
from sqlalchemy_utils import database_exists, create_database
from settings import DATABASE_URI
from models.todo_model import Base
from sqlalchemy.orm import sessionmaker

engine = db_orm.create_engine(DATABASE_URI)
_Session = sessionmaker(bind=engine)
if not database_exists(engine.url):
    create_database(engine.url)


def create_table():
    Base.metadata.create_all(engine)


def new_session():
    return _Session()
