from django.urls import path
from .views import CreditCardListCreateView, CreditCardDetailView

urlpatterns = [
    path("", CreditCardListCreateView.as_view(), name="card-list-create"),
    path("<int:pk>/", CreditCardDetailView.as_view(), name="card-detail"),
]