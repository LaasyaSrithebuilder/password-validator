
from django.urls import path
from core.views import login_view

urlpatterns = [
    path("api/login/", login_view),
]
