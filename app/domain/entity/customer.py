
from sqlalchemy import Column, String, Integer, Date
from app.domain.repository.database import Base
from sqlalchemy.orm import relationship, backref

from .order import Order

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    createdon = Column(Date)

    customer_orders = relationship('Order', primaryjoin="and_(Customer.id == Order.customerid)")    

    def __init__(self, id, firstName, lastName, email, createdOn):
        self.id = id
        self.firstname = firstName
        self.lastname = lastName
        self.email = email
        self.createdon = createdOn

    

        

