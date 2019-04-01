from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, DateTime, Text, Float)
from sqlalchemy.orm import sessionmaker
import datetime

from scrapy.utils.project import get_project_settings

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
formatter = logging.Formatter('[%(asctime)s, level: %(levelname)s, file: %(name)s, function: %(funcName)s], message: %(message)s')
file_handler = logging.FileHandler('unident/logs/models.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

Base = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

engine = db_connect()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


def check_existence_row_in_db(Title):
    return session.query(Product).filter(Product.Title == Title).scalar()


def get_price_from_databse(Title):
    try:
        p = session.query(Product).filter(Product.Title == CodeProduct).first()
        return p.Price
    except:
        logger.exception('Ошибка при получении информации о цене товара: ' + str(Title))


def insert_row_to_history_database(Title):
    try:
        session.execute('INSERT INTO History_Product (SELECT * FROM Product WHERE href="' + Title + '");')
        session.commit()
    except:
        logger.exception('Ошибка при записи товара в историческую БД: ' + str(Title))


def update_price(Title, price):
    try:
        session.query(Product).filter(Product.Title == Title).update(dict(price=price, created_date=datetime.datetime.first()))
        session.commit()
    except:
        logger.exception('Ошибка при обновлении цены товара ' + str(Title))



class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    Title = Column(String(200))
    Price =  Column(Float)
    Brand = Column(String(100))
    Artikul = Column(String(100))
    Code = Column(String(100))
    Country = Column(String(100))
    Description = Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Product(title= '%s')>" % self.Title


class HistoryProduct(Base):
    __tablename__ = "History_Product"

    id = Column(Integer, primary_key=True)
    Title = Column(String(200))
    Price =  Column(Float)
    Brand = Column(String(100))
    Artikul = Column(String(100))
    Code = Column(String(100))
    Country = Column(String(100))
    Description = Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<History_Product(title= '%s')>" % self.Title
