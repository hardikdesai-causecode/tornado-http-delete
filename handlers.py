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

class OrgHandler(tornado.web.RequestHandler):
    def get(self,user_uid,org_uid= None):

        response = dict(user_uid=user_uid)
        if org_uid:
            response[org_uid] = org_uid

        self.write(response)

    def delete(self,user_uid,org_uid):
        response = dict(user_uid=user_uid)
        if org_uid:
            response[org_uid] = org_uid

        self.write(response)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/uid/([-0-9a-fA-F]+)/org/?([-0-9a-fA-F]+)?", OrgHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()