from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:id>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
