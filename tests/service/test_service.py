
import unittest
from unittest import mock
import json

#from app.domain.repository.customer_repository import CustomerRepository
from app.service.customer_service import CustomerService
from app.domain.repository.db_utils import DBUtils
from tests.test_fixture import TestFixture
from tests.test_utils import TestUtils
from app.domain.repository.db_factory import DbFactory

class CustomerServiceTest(unittest.TestCase):

    @mock.patch('app.domain.repository.db_factory.DbFactory.get_db_instance')
    def test_get_customer_by_id_success(self, mock_db_instance):
        customer_repository_mock = mock.Mock()
        customer_repository_mock.find_by_id.return_value = TestFixture.get_customer()
        customer_service = CustomerService()
        customer_service.customer_repository = customer_repository_mock
        customer_json = customer_service.get_customer_by_id(1)
        customer_obj = json.loads(customer_json)
        self.assertEqual(customer_obj['id'], 1)  

    @mock.patch('app.domain.repository.db_factory.DbFactory.get_db_instance')
    def test_get_customer_list_success(self, mock_db_instance):
        customer_repository_mock = mock.Mock()

        meta_dict = DBUtils.get_paginator_dict()
        customer_repository_mock.find_all.return_value = [TestFixture.get_customer()], meta_dict

        customer_service = CustomerService()
        customer_service.customer_repository = customer_repository_mock
        
        customer_json = customer_service.get_customer_list(None, 1)
        customer_list_obj = json.loads(customer_json)
        customer_obj = json.loads(json.dumps(customer_list_obj['objects']))
        self.assertEqual(customer_obj[0]['id'], 1)  

    

