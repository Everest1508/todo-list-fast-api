from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    todos = fields.ReverseRelation["Todo"] 

    def __str__(self):
        return self.username

    class Meta:
        table = "users"
