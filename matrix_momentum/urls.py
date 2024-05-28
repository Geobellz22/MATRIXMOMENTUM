"""
URL configuration for matrix_momentum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# matrix_momentum/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Matrix Momentum API",
        default_version='v1',
        description="API for Matrix Momentum",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="st377126@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/portfolios/', include('portfolios.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/company-profiles/', include('company_profile.urls')),
    path('api/signals/', include('signals.urls')),
    path('api/users/', include('users.urls')),
    path('api/wallets/', include('wallets.urls')),
]