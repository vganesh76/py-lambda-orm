import unittest
import mock
import json

from app.service.customer_service import CustomerService
from app.domain.repository.customer_repository import CustomerRepository
from app.controller.router import Router
from tests.test_utils import TestUtils
from app.domain.repository.db_factory import DbFactory

class RouterTest(unittest.TestCase):

    @mock.patch('app.domain.repository.db_factory.DbFactory.get_db_instance')
    def test_get_customer_by_id_success(self, mock_db_instance):
        customer_service_mock = self.get_customer_service_mock()
        router = Router()
        router.customer_service = customer_service_mock
        result = router.handle_request(self.get_id_event(), None)
        self.assertEqual(result['body']['id'], 1)  

    @mock.patch('app.domain.repository.db_factory.DbFactory.get_db_instance')
    def test_get_customer_list_success(self, mock_db_instance):
        customer_service_mock = self.get_customer_service_mock()
        router = Router()
        router.customer_service = customer_service_mock
        result = router.handle_request(self.get_list_event(), None)
        self.assertEqual(result['body'][0]['id'], 1)  

    @mock.patch('app.domain.repository.db_factory.DbFactory.get_db_instance')
    def test_get_invalid_evet(self, mock_db_instance):
        customer_service_mock = self.get_customer_service_mock()
        router = Router()
        router.customer_service = customer_service_mock
        result = router.handle_request({'path': 'test1234'}, None)
        self.assertEqual(result['statusCode'], 400)  

    def get_customer_service_mock(self):
        customer_service_mock = mock.MagicMock(spec=CustomerService)
        mock_tuple = TestUtils.get_db_mock()
        db_mock = mock_tuple[0]
        customer_repository = mock.Mock()
        customer_repository.db = db_mock
        customer_service_mock.customer_repository = customer_repository

        customer_service_mock.get_customer_by_id.return_value = {'id':1, 'user_id':2345}
        customer_service_mock.get_customer_list.return_value = [{'id':1, 'user_id':2345}]
        return customer_service_mock

    def get_id_event(self):
        event = {
            "path":"/customer/1",
            "pathParameters":{
                "id":"6"
            },
        }

        return event  
    
    def get_list_event(self):
        event = {
            "path":"/customer",
        }

        return event
    