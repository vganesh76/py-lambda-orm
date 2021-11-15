import json
import logging

from app.domain.repository.customer_repository import CustomerRepository
from .service_utils import ServiceUtils
from app.domain.repository.db_factory import DbFactory
from app.model.customer_list import CustomerList

logger = logging.getLogger(__name__)

class CustomerService():
    def __init__(self):
        self.customer_repository = CustomerRepository(DbFactory.get_db_instance())

    def get_customer_by_id(self, id):
        logger.info('### Inside get_customer_by_id id: {0}'.format(id))
        try:
            customer_dict = self.customer_repository.find_by_id(id)
            customer_json = json.dumps(customer_dict, indent=4, default=ServiceUtils.json_date_coverter)
            logger.info('*** customer_json: \n {0}'.format(customer_json))
            return customer_json
        except Exception as ex:
            logger.error(ex)
            raise Exception("Error in get_customer_by_id: {0}".format(ex))

    def get_customer_list(self, limit, page):
        logger.info('### Inside get_customer_list ###')
        try:
            result_tuple = self.customer_repository.find_all(limit, page)
            customer_dict = result_tuple[0]
            meta_dict = result_tuple[1]
            customer_list = CustomerList.get_customer_list(meta_dict, customer_dict)
            customer_json = json.dumps(customer_list, indent=4, default=ServiceUtils.json_date_coverter)
            return customer_json
        except Exception as ex:
            logger.error(ex)
            raise Exception("Error in customer_list: {0}".format(ex))


