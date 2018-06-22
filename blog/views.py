from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Topic, Entry

# Create your views here.

class TopicsView(ListView):
    model = Topic

class OneTopicView(DetailView):
    model = Topic

class EntryView(DetailView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'blog/entry.html'

# trello
# jira