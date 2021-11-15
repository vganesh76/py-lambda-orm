import datetime

from app.domain.entity.customer import Customer
from .database import Database
from .db_utils import DBUtils

max_rows = 20

class CustomerRepository():

    def __init__(self, db):
        self.db = db

    def add(self, _customer):
        firstName = _customer['firstName']
        lastName = _customer['lastName']
        email = _customer['email']
        createdOn = datetime.datetime.now()
        customer_obj = Customer(firstName, lastName, email, createdOn)

        session = self.db.get_session()
        session.add(customer_obj)
        session.commit()
        session.close()

    def find_all(self, limit, page=1):
        session = None
        if limit is None:
            limit = max_rows
        try:
            session = self.db.get_session()
            query = session.query(Customer)
            limit = 5
            paginator = self.db.get_paginator(query, limit)
            meta_dict = DBUtils.get_pagination(limit, paginator, page)
            current_page = paginator.page(page)
            customers = current_page.object_list
            customer_list = []
            for customer in customers:
                customer_list.append(self.get_child_data(customer))
            return customer_list, meta_dict
        except Exception as ex:
            print("Failed to find_all: {0}".format(ex))
            raise Exception("Failed to find_all: {0}".format(ex))
        finally:
            if session:
                session.close()

    def find_by_id(self, id):
        session = self.db.get_session()
        customer = session.query(Customer) \
            .filter(Customer.id == id) \
            .first()
        customer_dict = DBUtils.object_as_dict(customer)
        orders = []
        for o in customer.customer_orders:
            orders.append(DBUtils.object_as_dict(o))
        customer_dict['customer_order'] = orders
        return customer_dict        

    def get_child_data(self, customer):       
        customer_orders = customer.customer_orders
        customer_orders_dict = []
        for rb in customer_orders:
            customer_orders_dict.append(DBUtils.object_as_dict(rb))
        customer_dict = DBUtils.object_as_dict(customer)
        customer_dict['customer_orders'] = customer_orders_dict
        return customer_dict     
