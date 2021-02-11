import tornado.ioloop
import tornado.web

class PatientHandler(tornado.web.RequestHandler):
    def get(self):
        print('heree')
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/patients", PatientHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()