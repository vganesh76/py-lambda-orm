import re
import logging

from app.service.customer_service import CustomerService

logger = logging.getLogger(__name__)

router_path_match_dict = {
    'find_by_id': r'^/customer/\d{1,10}$',
    'find_all': r'^/customer$'
}

class Router():
    def __init__(self):
        self.customer_service = CustomerService()
        self.router_map = {
            'find_by_id': lambda event : self.get_customer_by_id(event),
            'find_all': lambda event : self.get_customer_list(event)
        }

    def handle_request(self, event, context):
        path = event['path']
        print('*** path: {0}'.format(path))
        router_action = self.match_path(path)

        print('*** router_action: ', router_action)

        if router_action is not None:
            return self.router_map[router_action](event)
        else:
            return self.get_invalid_event()

    def match_path(self, path):
        for key in router_path_match_dict:
            value = router_path_match_dict[key]
            if re.search(value, path):
                return key

    def get_customer_by_id(self, event):
        logger.info('*** Inside get_customer_by_id ***')
        try:
            path_param = event['pathParameters']
            id = path_param['id']
            logger.info('***  id: {0}'.format(id))
            customer_json = self.customer_service.get_customer_by_id(id)

            return self.get_success_response(customer_json)
        except Exception as ex:
            raise ex

    def get_customer_list(self, event):
        print('*** Inside get_customer_list ***')
        try:
            try:
                path_param = event['pathParameters']
            except KeyError:
                path_param = None
            limit = None

            if path_param:
                limit = path_param['limit']
            customer_json = self.customer_service.get_customer_list(limit, 1)

            return self.get_success_response(customer_json)
        except Exception as ex:
            raise ex

    def get_success_response(self, body):
        return {
            'statusCode': 200,
            'body': body,
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    def get_invalid_event(self):
        return {
            'statusCode': 400,
            'body': {'error': 'Invalid Request'},
            'headers': {
                'Content-Type': 'application/json',
            },
        }
