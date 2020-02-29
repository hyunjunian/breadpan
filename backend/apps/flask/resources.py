""" Resource packages

- Represents the resource to expose via HTTP.
- This layer is outterrior of software depending on the framework.
- So implements the resource class for 
"""

from http import HTTPStatus
from flask_restful import reqparse, abort, Resource
from .context import todo

todoCtrl = todo.ToDoController()  # todo컨트롤러를 불러온다.
parser = reqparse.RequestParser()
parser.add_argument('task')


def abort_if_todo_doesnt_exist(todo_id):
    try:
        todoCtrl.read(todo_id)
    except:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class FlaskTodoController(Resource):

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return todoCtrl.read(todo_id), HTTPStatus.OK

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todoCtrl.delete(todo_id)
        return '', HTTPStatus.NO_CONTENT

    def put(self, todo_id):  # Flask에서 request 를 받아서 처리
        args = parser.parse_args()  # request 의 arg 받아오기
        task = {'task': args['task']}  # ToDoUpdateInteractor에서 사용할 수 있는 형태로 데이터를 전달하기 위해 데이터 형태 변경 (질문: 왜 ToDoUpdateInteractor에 맞게 변경해야하는가? Inputport에 맞게 해야하는 것 아닌가?)
        todoCtrl.update(todo_id, task)  # todo컨드롤러의 업데이트 메소드 실행
        return task, HTTPStatus.CREATED


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class FlaskTodoListController(Resource):
    def get(self):
        return todoCtrl.read_all_data(), HTTPStatus.OK

    def post(self):
        args = parser.parse_args()
        all_data = todoCtrl.read_all_data()

        todo_id = len(all_data) + 1
        todo_id = 'todo%i' % todo_id
        task = {'task': args['task']}

        t = todoCtrl.create(todo_id, task)
        return t, HTTPStatus.CREATED
