from flask import Flask
from flask_restful import Api
from apps.flask.resources import FlaskTodoListController,FlaskTodoController

app = Flask(__name__)
api = Api(app)


##
# Actually setup the Api resource routing here
##

api.add_resource(FlaskTodoListController, '/todos')
api.add_resource(FlaskTodoController, '/todos/<todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
