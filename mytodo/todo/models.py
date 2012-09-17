from django.db import models
import datetime

PRIORITY_CHOICES = (
    (1,'Low'),
    (2,'Normal'),
    (3,'High'),
)

class List(models.Model):
    title = models.CharField(max_length=40,unique=True)
    def __unicode__(self):
        return self.title
    class META:
        ordering = ['title']

class Item(models.Model):
    title = models.CharField(max_length=40)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    due_date = models.DateTimeField(blank=True,null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(List)
    def __unicode__(self):
        return self.title
    class META:
        ordering = ['-priority','title']
