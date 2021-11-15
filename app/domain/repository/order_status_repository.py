
from app.domain.entity.order_status import OrderStatus
from .database import Database

class OrderStatusRepository():

    def __init__(self, db):
        self.db = db

    def find_all(self):
        print('*** Inside find_all ***')
        session = self.db.get_session()
        order_status = session.query(OrderStatus).all()
        print('*** order_status: ', order_status)
        #order_status_dict = self.db.object_as_dict(order_status)
        #print('*** order_status: ', order_status_dict)
        order_status_list = []
        for o in order_status:
            order_status_list.append(self.db.object_as_dict(o))
        return order_status_list       

    def find_by_status(self, status):
        print('*** Inside find_by_status ***')
        session = self.db.get_session()
        order_status = session.query(OrderStatus) \
            .filter(OrderStatus.status == status) \
            .first()
        order_status_dict = self.db.object_as_dict(order_status)
        print('*** order_status: ', order_status_dict)
        return order_status_dict        