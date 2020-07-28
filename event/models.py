from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.link
