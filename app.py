from flask import Flask
from flask_restful import Api

from src.web import HelloResource

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
