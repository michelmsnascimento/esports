from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.torneios, name="torneios"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)