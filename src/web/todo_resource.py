from flask_restful import Resource, abort

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


# Single Todo Data Resource
class TodoResource(Resource):
    # Get Todo List to Index
    def get(self, todo_id):
        __checked_todo_index__(todo_id=todo_id)
        return TODOS[todo_id]


# Todo List Resource
class TodoListResource(Resource):
    # Get Todo All List
    def get(self):
        return TODOS
