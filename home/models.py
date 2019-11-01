from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField(max_length=5000)

    def __str__(self):
        return self.name