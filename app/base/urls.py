from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
	path('add', views.add, name='add'),
	path('result/<str:id>', views.get_task, name='get_task'),

]
