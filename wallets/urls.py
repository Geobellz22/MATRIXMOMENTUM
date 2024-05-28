from django.urls import path
from .views import get_wallet, create_wallet, update_wallet, delete_wallet
urlpatterns = [
    path('', get_wallet),
    path('create/', create_wallet),
    path('<int:pk>/', get_wallet),
    path('<int:pk>/update/', update_wallet),
    path('<int:pk>/delete/', delete_wallet),
]
