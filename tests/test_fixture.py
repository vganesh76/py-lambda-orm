
import datetime
import psycopg2

from app.domain.entity.customer import Customer

customer_dict = {
            'id': 1,
            'firstName': 'John',
            'lastName': 'Kerry',
            'email': 'test@test.com',
            'createdOn': datetime.datetime.now()
        }

class TestFixture():

    @staticmethod
    def get_customer():
        return customer_dict

    @staticmethod
    def get_customer_entity():
        return Customer(**customer_dict)