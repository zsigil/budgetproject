from django.urls import path
from . import views

app_name = "budget"

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:projectslug>', views.project_detail, name="project_detail"),
]
