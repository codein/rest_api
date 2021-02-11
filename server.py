import tornado.ioloop
import tornado.web
import json
import logging

def get_logger(name):
    FORMAT = '%(asctime)-15s %(name)s %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    logger = logging.getLogger(name)
    return logger

logger = get_logger('handler')

class JsonRequestHandler(tornado.web.RequestHandler):
    """Base Handler with capabiblity to write json data back"""

    @property
    def logger(self):
        if not hasattr(self, '_logger'):
            self._logger = get_logger('handler')

        return self._logger

    @property
    def store(self):
        """store property from the main application object is referenced"""
        if not hasattr(self, '_store'):
            self._store = self.application.store

        return self._store

    def json_write(self, data):
        """Given a python dict wraps it in a data attribute and returned."""
        self.write(json.dumps(data))

    def json_loads(self):
        return json.loads(self.request.body)

class PatientHandler(JsonRequestHandler):

    def get(self, patient_id):
        if patient_id in self.store:
            patient_obj = self.store[patient_id]
            self.logger.info('Found patient_id {0}'.format(patient_id))
            self.write(patient_obj)
        else:
            self.logger.error('Not Found')
            raise tornado.web.HTTPError(status_code=404, log_message='Not Found')

    def put(self):
        patient_obj = self.json_loads()
        patient_id = str(self.application.next_id)
        patient_obj['id'] =patient_id
        self.store[patient_id] = patient_obj
        self.application.increment_next_id()
        self.logger.info('Saved patient_id {0}'.format(patient_id))
        self.json_write(patient_obj)


class REST_API_Application(tornado.web.Application):
    """Main application with store singleton is an attribute of this object."""
    handlers = [
        (r"/patients", PatientHandler),
        (r"/patients/*([a-zA-Z0-9-]*)", PatientHandler),
    ]

    def __init__(self):
        tornado.web.Application.__init__(self, self.handlers, debug=True)

    @property
    def store(self):
        """instantiates the store dict."""
        if not hasattr(self, '_store'):
            self._store = {}

        return self._store

    @property
    def next_id(self):
        if not hasattr(self, '_next_id'):
            self._next_id = 1

        return self._next_id

    def increment_next_id(self):
        self._next_id += 1

if __name__ == "__main__":
    application = REST_API_Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()