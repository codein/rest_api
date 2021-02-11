import requests
import datetime
import unittest

import logging

def get_logger(name):
    FORMAT = '%(asctime)-15s %(name)s %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger(name)
    return logger


class REST_API_Client(object):
    """REST_API_Client warps API endpoints into functions"""
    def __init__(self, *args, **kwargs):
        super(REST_API_Client, self).__init__()
        self.logger = get_logger('API-client')
        self.patient_url = 'http://localhost:8888/patients'

    def get_patient(self, patient_id):
        url = '{0}/{1}'.format(self.patient_url, patient_id)
        self.logger.info('GET:{0}'.format(url))
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            response_json = response.json()
            self.logger.info('Found {0} objects'.format(len(object_list)))
            return response.json()
        else:
            raise RuntimeError('Failed GET:{0}'.format(url))

    def put_patient(self, patient_id, patient_dict):
        pass

    def post_patient(self):
        pass

class Test_patient_endpoint(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        "set up test fixtures"
        self.rest_api_client = REST_API_Client()

    def test_get(self):
        print(self.rest_api_client.get_patient(1))

if __name__ == '__main__':
    unittest.main()