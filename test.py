import requests
import datetime
import unittest
import json
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
            self.logger.info('Found {0} object'.format(response_json))
            return response_json
        else:
            raise RuntimeError('Failed GET:{0}'.format(url))

    def put_patient(self, patient_obj):
        url = self.patient_url
        self.logger.info('PUT:{0}'.format(url))
        response = requests.put(url, json.dumps(patient_obj) )
        if response.status_code == requests.codes.ok:
            response_json = response.json()
            self.logger.info('Found {0} object'.format(response_json))
            return response_json
        else:
            raise RuntimeError('Failed PUT:{0}'.format(url))


    def post_patient(self):
        pass

class Test_patient_endpoint(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        "set up test fixtures"
        self.rest_api_client = REST_API_Client()

    def test_scenario_1(self):
        patient_obj = {
            'first_name': 'first_name_1',
            'last_name': 'last_name',
            'date_of_birth': 'date_of_birth',
            'phone_number': 'phone_number',
        }
        patient_obj = self.rest_api_client.put_patient(patient_obj)
        observed = patient_obj['id']
        expected = '1'
        self.assertEqual(observed, expected, "Should be equal")

        patient_obj = self.rest_api_client.get_patient('1')
        observed = patient_obj['id']
        expected = '1'
        self.assertEqual(observed, expected, "Should be equal")

        observed = patient_obj['first_name']
        expected = 'first_name_1'
        self.assertEqual(observed, expected, "Should be equal")


    def test_scenario_2(self):
        patient_obj = {
            'first_name': 'first_name_2',
            'last_name': 'last_name',
            'date_of_birth': 'date_of_birth',
            'phone_number': 'phone_number',
        }
        patient_obj = self.rest_api_client.put_patient(patient_obj)
        observed = patient_obj['id']
        expected = '2'
        self.assertEqual(observed, expected, "Should be equal")

        patient_obj = self.rest_api_client.get_patient('1')
        observed = patient_obj['id']
        expected = '1'
        self.assertEqual(observed, expected, "Should be equal")

        observed = patient_obj['first_name']
        expected = 'first_name_1'
        self.assertEqual(observed, expected, "Should be equal")

        patient_obj = self.rest_api_client.get_patient('2')
        observed = patient_obj['id']
        expected = '2'
        self.assertEqual(observed, expected, "Should be equal")

        observed = patient_obj['first_name']
        expected = 'first_name_2'
        self.assertEqual(observed, expected, "Should be equal")



if __name__ == '__main__':
    unittest.main()