from django.urls import path
from .views import CompanyProfileListCreateAPIView, CompanyProfileRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CompanyProfileListCreateAPIView.as_view()),
    path('<int:pk>/', CompanyProfileRetrieveUpdateDestroyAPIView.as_view()),
]