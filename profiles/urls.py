from django.urls import path
from .views import get_user_profiles, create_user_profile, get_user_profile, update_user_profile, delete_user_profile

urlpatterns = [
    path('', get_user_profiles),
    path('create/', create_user_profile),
    path('<int:pk>/', get_user_profile),
    path('<int:pk>/update/', update_user_profile),
    path('<int:pk>/delete/', delete_user_profile),
]