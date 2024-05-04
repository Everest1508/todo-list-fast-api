from tortoise.models import Model
from tortoise.fields import *
from api.models.user import User

class Todo(Model):
    id = IntField(pk=True)
    task = CharField(max_length=100, null=False)
    done = BooleanField(default=False, null=False)
    user = ForeignKeyField("models.User", related_name="todos")  
    class PydanticMeta:
        exclude = ["user"]
    # created_at = DatetimeField(auto_now_add=True)
    # updated_at = DatetimeField(auto_now=True)
