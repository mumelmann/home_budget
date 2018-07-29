from django.urls import path
from budget_app import views

urlpatterns = [
    path('', views.project_list, name='list'),
    path('<int:p_id>/', views.project_detail, name='detail'),
]
