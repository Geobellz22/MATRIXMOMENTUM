from django.urls import path
from .views import PortfolioListCreateAPIView, PortfolioRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PortfolioListCreateAPIView.as_view()),
    path('<int:pk>/', PortfolioRetrieveUpdateDestroyAPIView.as_view()),
    
]
