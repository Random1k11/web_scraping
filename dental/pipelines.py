from sqlalchemy.orm import sessionmaker
from dental.models import db_connect, create_table, Product, HistoryProduct, check_existence_row_in_db,\
                                get_price_from_databse, insert_row_to_history_database, update_price
from sqlalchemy.exc import IntegrityError

import logging

logger = logging.getLogger('pipeline')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s, level: %(levelname)s, file: %(name)s, function: %(funcName)s], message: %(message)s')
file_handler = logging.FileHandler('dental/logs/pipeline.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)


class DentalSpiderPipeline(object):

    def __init__(self):

        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        session = self.Session()
        productDB = Product()
        productDB.Title              = item["Title"]
        productDB.Price              = item["Price"]
        productDB.Brand              = item["Brand"]
        productDB.Artikul            = item["Artikul"]
        productDB.Code               = item["Code"]
        productDB.Country            = item["Country"]
        productDB.Description        = item["Description"]
        productDB.Main_section       = item["Main_section"]
        productDB.Sub_section        = item["Sub_section"]
        productDB.Under_sub_section  = item["Under_sub_section"]

        productDB.Href         = item["Href"]

        try:
            if check_existence_row_in_db(productDB.Href) == None:
                logger.debug('=== Записываю в БД новый товар ===')
                session.add(productDB)
                session.commit()
            else:
                if int(productDB.Price) != int(get_price_from_databse(productDB.Href)):
                    logger.info('=== Цена товара изменилась ===')
                    try:
                        insert_row_to_history_database(productDB.Href)
                        logger.info('=== Записываю в таблицу с историей ===')
                    except IntegrityError:
                        pass
                    update_price(productDB.Href, productDB.Price)
                    logger.info('=== Цена товара обновлена ===')

        except:
            session.rollback()
            raise
        finally:
            session.close()
