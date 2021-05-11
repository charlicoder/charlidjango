from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('login/', TemplateView.as_view(template_name="index.html"), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("", include("aaa.urls")),
]
