# from django.urls import path
# from .views import TransactionHistoryView

# urlpatterns = [
#     path("", TransactionHistoryView.as_view(), name="transaction-history"),
# ]
from django.urls import path

from .views import (
    TransactionHistoryView,
    TransactionCSVExportView,
)

urlpatterns = [
    path("", TransactionHistoryView.as_view(), name="transaction-history"),
    path(
        "export/",
        TransactionCSVExportView.as_view(),
        name="transaction-export",
    ),
]