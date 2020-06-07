from flask.views import MethodView


class Hello(MethodView):

    def get(self):
        return '<h1>Hello World</h1>'