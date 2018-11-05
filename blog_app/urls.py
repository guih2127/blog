from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list')
]

# atribuimos uma view (post_list) para a URL raíz ('')