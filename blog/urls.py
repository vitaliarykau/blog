from django.contrib import admin
from django.urls import path, include
from .views import EntryView

app_name = 'blog'

urlpatterns = [
    # path('topic/', TopicView.as_view(), name='topics'),
    path('topic/entry<int:pk>/', EntryView.as_view(), name='entry'),
]
