from breadpan.usecase import DataAccessGateway, UsecaseInteractor, UsecaseOutputPort
from todo.entity import ToDoEntity


class ToDoCreateInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get id from the controller's data. 
        todo_id = self.input["todo_id"]
        contents = self.input["contents"]
        t = ToDoEntity(todo_id, contents['task'])

        # Store the data. 
        data.create(t)

        # Link to output port
        return UsecaseOutputPort(todo=t)


class ToDoUpdateInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get id from the controller's data. 
        todo_id = self.input["todo_id"]  # InputPort 에서 만들어 둔 Interface 에 맞게 데이터 받은 뒤, 해당 데이터를 메소드 안의 변수로 받기
        contents = self.input["contents"]
        t = ToDoEntity(todo_id, contents['task'])  # Todo엔티티를 이용하여 엔티티 생성

        # Store the data. 
        data.update(t)

        # Link to output port
        return UsecaseOutputPort(todo=t)


class ToDoReadInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get task ID
        todo_id = self.input["todo_id"]

        # Read data.
        t = data.read(entity_id=todo_id)

        # Return the entity via UsecaseOutputPort.
        return UsecaseOutputPort(todo=t)


class ToDoReadAllInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        return UsecaseOutputPort(todo=data.read_all())


class ToDoDeleteInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get task ID
        todo_id = self.input["todo_id"]

        # Delete data by entity id. 
        data.delete(todo_id)

        return UsecaseOutputPort()
