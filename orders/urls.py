from django.urls import path
from .views import order_list, order_create, order_detail, order_update, order_delete

urlpatterns = [
    path('', order_list),
    path('create/', order_create),
    path('<int:pk>/', order_detail),
    path('<int:pk>/update/', order_update),
    path('<int:pk>/delete/', order_delete),
]