from django.urls import path
from .views import signal_list, signal_create, signal_detail, signal_update, signal_delete

urlpatterns = [
    path('', signal_list),
    path('create/', signal_create),
    path('<int:pk>/', signal_detail),
    path('<int:pk>/update/', signal_update),
    path('<int:pk>/delete/', signal_delete),
]
