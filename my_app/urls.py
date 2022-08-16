from django.urls import path

urlpatterns = [
    path('', 'myapp.views.hello', name='hello')
]
