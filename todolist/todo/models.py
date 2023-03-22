from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=500)
    status = models.BooleanField()

    class Meta:
        db_table = 'todo'
