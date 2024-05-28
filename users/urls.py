from django.urls import path
from .views import get_users, create_user, get_user, update_user, delete_user

urlpatterns = [
    path('', get_users),
    path('create/', create_user),
    path('<int:pk>/', get_user),
    path('<int:pk>/update/', update_user),
    path('<int:pk>/delete/', delete_user),
]
