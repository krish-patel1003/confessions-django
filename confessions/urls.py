from django.urls import path
from .views import *


urlpatterns = [
    path('', ConfListView.as_view(), name="confessions-home"),
    path('create_confession/', ConfCreateView.as_view(), name='confession-create'),
    path('confession-detail/<int:pk>/', ConfDetailView.as_view(), name='confession-detail'),
    path('confession-update/<int:pk>', ConfUpdateView.as_view(), name='confession-update'),
    path('confession-delete/<int:pk>', ConfDeleteView.as_view(), name='confession-delete')
]
