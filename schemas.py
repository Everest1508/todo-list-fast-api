from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)

class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
