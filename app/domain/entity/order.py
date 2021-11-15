from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.domain.repository.database import Base
from .order_status import  OrderStatus

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    orderdate = Column(Date)
    completeddate = Column(Date)

    statusid = Column(Integer, ForeignKey('order_status.id'))
    customerid = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer', primaryjoin="and_(Customer.id == Order.customerid)")
    status = relationship('OrderStatus', primaryjoin="and_(OrderStatus.id == Order.statusid)")

    def __init__(self, statusid, orderdate, completeddate, customer_id):
        self.statusid = statusid
        self.orderdate = orderdate
        self.completeddate = completeddate
        self.customerid = customer_id

    
