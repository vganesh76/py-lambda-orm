
import unittest
from unittest import mock
from sqlalchemy.orm import Session, Query
from sqlalchemy_paginator import Paginator

from tests.test_fixture import TestFixture
from app.domain.repository.customer_repository import CustomerRepository
from tests.test_utils import TestUtils

class CustomerRepositoryTest(unittest.TestCase):

    def test_find_by_id_success(self):
        mock_tuple = TestUtils.get_filter_mock()
        db_mock = mock_tuple[0]

        customer_repo = CustomerRepository(db_mock)
        ret_1 = customer_repo.find_by_id(1)
        self.assertEqual(ret_1['id'], 1)  

    @mock.patch('app.domain.repository.customer_repository.CustomerRepository.find_by_id', side_effect=Exception('Error in DB connection'))
    def test_find_by_id_exception(self, find_by_id):
        with self.assertRaises(Exception):
            find_by_id(1234)

    def test_find_all_success(self):
        mock_tuple = TestUtils.get_db_mock()
        db_mock = mock_tuple[0]
        mock_session = mock_tuple[1]
        mock_paginator = mock_tuple[2]
        customer = TestFixture.get_customer_entity()  

        mock_query = mock_session.query()
        mock_current_page = mock.Mock()
        mock_paginator.page.return_value = mock_current_page
        mock_current_page.object_list = [customer]

        customer_repo = CustomerRepository(db_mock)
        result_tuple = customer_repo.find_all(None, 1)
        ret_list = result_tuple[0]
        self.assertEqual(ret_list[0]['id'], 1)  

    @mock.patch('app.domain.repository.customer_repository.CustomerRepository.find_all', side_effect=Exception('Error in DB connection'))
    def test_find_all_exception(self, find_all):
        with self.assertRaises(Exception):
            find_all(None, 1)


if __name__ == '__main__':
     unittest.main()
