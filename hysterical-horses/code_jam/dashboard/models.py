from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    Model for messages in instant messenger
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.content) <= 15:
            title = self.content
        else:
            title = self.content[:15]

        return f'{self.author}: {title}'