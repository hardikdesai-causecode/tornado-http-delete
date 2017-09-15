import tornado.ioloop
import tornado.web
import tornado.escape

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sample.html")

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        name = data['name']
        age = data['age']
        response = dict(
            name = name,
            age = age
        )
        self.write(response)

    def delete(self):
        data = tornado.escape.json_decode(self.request.body)
        name = data['name']
        age = data['age']
        response = dict(
            name=name,
            age=age
        )
        self.write(response)

    def put(self):
        data = tornado.escape.json_decode(self.request.body)
        name = data['name']
        age = data['age']
        response = dict(
            name=name,
            age=age
        )
        self.write(response)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()