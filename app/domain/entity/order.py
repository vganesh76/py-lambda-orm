from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.domain.repository.database import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    orderdate = Column(Date)
    completeddate = Column(Date)

    statusid = Column(Integer, ForeignKey('order_status.id'))
    customerid = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer', backref=backref('orders', uselist=False))
    status = relationship('OrderStatus', backref=backref('orders', uselist=False))

    def __init__(self, statusid, orderdate, completeddate, customer_id):
        self.statusid = statusid
        self.orderdate = orderdate
        self.completeddate = completeddate
        self.customerid = customer_id

    
