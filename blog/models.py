from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    tag = models.CharField(max_length=30)
    # entry = models.ManyToManyField(Entry, related_name='tags')

    def __str__(self):
        return self.tag

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    authors = models.ManyToManyField(User)

    def __str__(self):
        return self.text if len(self.text) < 50 else (self.text[:50] + '...')

    class Meta:
        verbose_name_plural = 'Entries'

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    # author = models.ForeignKey('Users', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text if len(self.text) < 50 else (self.text[:50] + '...')


