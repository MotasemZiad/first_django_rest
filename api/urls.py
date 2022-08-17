from django.urls import path
from . import view

urlpatterns = [
    path('', view.get_data),
    path('add/', view.add_item),
]
