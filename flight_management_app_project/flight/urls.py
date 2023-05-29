from django.urls import path
from . import views

urlpatterns = [
    path('<id_vuelo>', views.detail, name='detail'),
    path('<id_vuelo>/bookflight', views.bookflight, name='bookflight'),
]