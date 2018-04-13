from django.db import models

class Apı_class(models.Model):
    content=models.TextField(max_length=120)

    def __str__(self):
        return self.content
