from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('safety/', views.safety, name='safety'),
    path('statistics/', views.statistics, name='statistics'),
    path('location/', views.location, name='location'),
    path('setting/', views.setting, name='setting'),
    path('popup/', views.popup, name='popup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)