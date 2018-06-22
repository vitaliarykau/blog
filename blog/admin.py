from django.contrib import admin
from .models import Entry, Comment, Tag


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    list_display = ('title', 'text', 'date_added')
    list_filter = ('date_added', )
    ordering = ('date_added',)
    autocomplete_fields = ('authors',)
    #readonly_fields = ('authors',)
    #raw_id_fields = ("tags",) # just a numbers (ids)
    #exclude = ('text',
    search_fields = ['title', 'text']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
#admin.site.register(PersonAdmin)
