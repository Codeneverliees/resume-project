from django.urls import path
from . import views
urlpatterns=[
 path('project/', views.services, name='project')
]