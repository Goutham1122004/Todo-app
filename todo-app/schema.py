import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Todo as TodoModel, db

class TodoObject(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel

class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoObject)

    def resolve_all_todos(self, info):
        return TodoModel.query.all()

class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.String(required=True)

    todo = graphene.Field(lambda: TodoObject)

    def mutate(self, info, title, description, time):
        todo = TodoModel(title=title, description=description, time=time)
        db.session.add(todo)
        db.session.commit()
        return CreateTodo(todo=todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
