import csv

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializer import TransactionSerializer


class TransactionHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.all().order_by("-created_at")

        # Status filter
        status = request.query_params.get("status")
        if status:
            transactions = transactions.filter(
                status=status.upper()
            )

        # Amount filter
        amount = request.query_params.get("amount")
        if amount:
            transactions = transactions.filter(
                amount=amount
            )

        # Date filter
        date = request.query_params.get("date")
        if date:
            transactions = transactions.filter(
                created_at__date=date
            )

        serializer = TransactionSerializer(
            transactions,
            many=True
        )

        return Response(serializer.data)


class TransactionCSVExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.all().order_by("-created_at")

        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="transactions.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Card ID",
            "Amount",
            "Status",
            "Created At",
        ])

        for transaction in transactions:
            writer.writerow([
                transaction.id,
                transaction.card_id,
                transaction.amount,
                transaction.status,
                transaction.created_at,
            ])

        return response