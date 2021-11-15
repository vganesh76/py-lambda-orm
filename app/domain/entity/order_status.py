from sqlalchemy import Column, String, Integer

from app.domain.repository.database import Base

class OrderStatus(Base):
    __tablename__ = 'order_status'
    id = Column(Integer, primary_key=True)
    status = Column(String)

    def __init__(self, status):
        self.status = status
