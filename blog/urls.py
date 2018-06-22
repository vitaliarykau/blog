from django.urls import path
from .views import EntryView, EntriesView, EditEntryView, AddEntryView
app_name = 'blog'

urlpatterns = [
    path('', EntriesView.as_view(), name='entries'),
    path('entry<int:pk>/', EntryView.as_view(), name='entry'),
    path('entry<int:pk>/edit', EditEntryView.as_view(), name='edit_entry'),
    path('entry/add', AddEntryView.as_view(), name='new_entry'),

]
