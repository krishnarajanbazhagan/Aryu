from django.urls import path, re_path 
from apps.home import admin, views

urlpatterns = [
    path('', views.index, name='home'),

    # Other specific URL patterns for your views
    path('emp', views.emp),  
    path('show', views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    re_path(r'^.*\.*', views.pages, name='pages'),

    # Your regex-based URL pattern
    #re_path(r'^.*\.*', views.pages, name='pages'),
]
