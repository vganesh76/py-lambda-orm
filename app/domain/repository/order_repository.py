import datetime
import logging

from app.domain.entity.order import Order
from .database import Database

logger = logging.getLogger()

class OrderRepository():

    def __init__(self, db):
        self.db = db

    def add(self, _order):
        logger.info('*** Inside order add ***')
        status_id = _order['statusid']
        customer_id = _order['customerid']
        order_date = datetime.datetime.now()
        order_obj = Order(status_id, order_date, None, customer_id)

        session = self.db.get_session()
        session.add(order_obj)
        session.commit()
        session.close()
        logger.info('*** Order added to DB ***')

    def find_all(self):
        logger.info('*** Inside order find_all ***')
        session = self.db.get_session()
        orders = session.query(Order).all()
        order_list = []
        for c in orders:
            order_list.append(self.db.object_as_dict(c))
        return order_list       

    def find_by_id(self, id):
        logger.info('*** Inside find_by_id ***')
        session = self.db.get_session()
        order = session.query(Order) \
            .filter(Order.id == id) \
            .first()
        order_dict = self.db.object_as_dict(order)
        logger.info('*** order: ', order_dict)
        return order_dict        