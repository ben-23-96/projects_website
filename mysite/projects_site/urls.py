from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:project_id>/', views.project_page, name='project_page'),
]

urlpatterns += staticfiles_urlpatterns()
