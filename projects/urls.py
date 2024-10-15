from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ProjectListview.as_view(),name='project_list'),
    path('project/create',views.ProjectCreateview.as_view(),name='project_create')
    
]