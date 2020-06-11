from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
	path('', views.index, name='index'), 
	path('vote/<poll_id>/', views.vote, name='vote'), 
	path('add/', views.add_poll, name='add_poll'), 
]