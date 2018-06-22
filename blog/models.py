from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=30)


    def __str__(self):
        return self.tag

    def natural_key(self):
        return self.tag

class Entry(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tags', null=True)
    authors = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.title if len(self.title) < 50 else (self.title[:50] + '...')

    class Meta:
        verbose_name_plural = 'Entries'


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text if len(self.text) < 50 else (self.text[:50] + '...')


