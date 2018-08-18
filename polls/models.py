from django.db import models


# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    forgotten = models.BooleanField(default=False)

    def __str__(self):
        return self.name
