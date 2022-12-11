from flask import request
from flask_restful import Resource, abort, reqparse

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


# checked to todo_index
def __checked_todo_index__(todo_id):
    if todo_id not in TODOS:
        abort(
            404,
            message="Todo id {} is not found".format(todo_id)
        )


parser = reqparse.RequestParser()
parser.add_argument('task')


# Single Todo Data Resource
class TodoResource(Resource):

    # Get Todo List to Index
    def get(self, todo_id):
        __checked_todo_index__(todo_id=todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        __checked_todo_index__(todo_id=todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        try:
            body = parser.parse_args()
        except Exception as e:
            return {"error": str(e)}
        task = body['task']
        TODOS[todo_id] = task
        return task, 201


# Todo List Resource
class TodoListResource(Resource):
    # Get Todo All List
    def get(self):
        return TODOS

    def post(self):
        try:
            args = parser.parse_args()
        except Exception as e:
            return {"error": str(e)}
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
