from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
	path('', views.index, name='index'), 
	path('add/', views.add_poll, name='add_poll'), 
	path('vote/<int:poll_id>/', views.vote, name='vote'), 
	path('results/<int:poll_id>/', views.results, name='results'),
	
]