from django.urls import path
from .views import WaterJugView

urlpatterns = [
    path('waterjug/', WaterJugView.as_view(), name='waterjug'),
]