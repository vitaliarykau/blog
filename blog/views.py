from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Entry, Tag

# Create your views here.

"""
class EntryView(DetailView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'blog/entry.html'
"""

# ----------------------------------
def convert_body(request):
    """ Convert a request body from format:
    title=some+text&next=another+text
    to dictionary
    """
    body_unicoded = request.body.decode('utf-8')
    body = body_unicoded.replace('&', '=')
    body = body.replace('+', ' ')
    body = body.split('=')

    keys = [body[i].strip() for i in range(len(body)) if i % 2 == 0]
    values = [body[i].strip() for i in range(1, len(body)) if i % 2 != 0]
    dict_of_values = {keys[i]:values[i] for i in range(len(keys)) if values[i] != ""}

    return dict_of_values


class EntriesView(ListView):
    #model = Entry
    #template_name = 'blog/homepage.html'
    #context_object_name = 'entries'
    def get(self, request, *args, **kwargs):
        data = serializers.serialize('json', Entry.objects.all(),
                                     use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return HttpResponse(data)


class EntryView(View):

    def get(self, request, pk,  *args, **kwargs):
        data = serializers.serialize('json', Entry.objects.filter(pk=pk),
                                     use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return HttpResponse(data)

class AddEntryView(CreateView):
    model = Entry
    template_name = 'blog/new_entry.html'
    success_url = reverse_lazy('blog:entries')
    fields = ['title', 'text', 'tags', 'authors']

    def post(self, request, *args, **kwargs):
        """ Create object via POST method"""

        dict_of_values = convert_body(request)

        new = Entry.objects.create(title=dict_of_values['title'], text=dict_of_values['text'])
        tags = [Tag.objects.get(pk=int(i)) for i in dict_of_values['tags'] if i != ' ']
        authors = [User.objects.get(pk=int(i)) for i in dict_of_values['authors'] if i != ' ']
        new.authors.set(authors)
        dict_of_values['tags'] = dict_of_values['tags'].split()
        new.tags.set(tags)

        data = serializers.serialize('json', Entry.objects.filter(pk=new.id),
                                     use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return HttpResponse('CREATED <p> {} </p>'.format(data))


class EditEntryView(UpdateView):
    model = Entry
    #form_class = EntryForm
    fields = ['title', 'text', 'tags', 'authors']
    template_name = 'blog/edit_entry.html'
    success_url = reverse_lazy('blog:entries')


    def post(self, request, *args, **kwargs):
        """ Update object via POST method"""

        self.object = self.get_object()
        last_data = serializers.serialize('json', Entry.objects.filter(pk=self.object.id),
                                          use_natural_foreign_keys=True, use_natural_primary_keys=True)

        dict_of_values = convert_body(request)

        for key in dict_of_values:
            if key == 'tags':
                tags = [Tag.objects.get(pk=int(i)) for i in dict_of_values['tags'].split()]
                self.object.tags.set(tags)
            elif key == 'authors':
                authors = [User.objects.get(pk=int(i)) for i in dict_of_values['authors'].split()]
                self.object.authors.set(authors)
            else:
                self.object.__dict__[key] = dict_of_values[key]
        self.object.save()

        data = serializers.serialize('json', Entry.objects.filter(pk=self.object.id),
                                     use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return HttpResponse('UPDATED <p>FROM {} </p><p> TO {} </p>'.format(last_data, data))






