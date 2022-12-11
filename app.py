from flask import Flask
from flask_restful import Api

from src.web import HelloResource, TodoListResource, TodoResource

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoResource, '/todos/<string:todo_id>')
api.add_resource(TodoListResource, '/todos')
api.add_resource(HelloResource, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
