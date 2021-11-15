
from unittest import mock
from sqlalchemy.orm import Session, Query
from sqlalchemy_paginator import Paginator

from tests.test_fixture import TestFixture

class TestUtils():
    @staticmethod
    def get_db_mock():
        db = mock.MagicMock()
        session = mock.MagicMock(spec=Session)
        db.get_session.return_value = session
        query = mock.MagicMock(spec=Query)
        session.query.return_value = query
        mock_paginator = mock.MagicMock(spec=Paginator)
        mock_paginator.page.return_value = mock.Mock()
        db.get_paginator.return_value = mock_paginator

        return db, session, mock_paginator

    @staticmethod
    def get_filter_mock():
        mock_tuple = TestUtils.get_db_mock()
        db_mock = mock_tuple[0]
        mock_session = mock_tuple[1]
        mock_query = mock_session.query()
        mock_filter = mock.Mock()
        mock_query.filter.return_value = mock_filter
        customer = TestFixture.get_customer_entity()   
        mock_filter.first.return_value = customer

        return db_mock, mock_filter
