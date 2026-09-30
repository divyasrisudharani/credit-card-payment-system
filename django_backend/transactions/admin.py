from django.contrib import admin, messages
from django.db.models import Sum, Count

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "card_id",
        "amount",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "card_id",
        "status",
    )

    ordering = (
        "-created_at",
    )

    actions = [
        "daily_payment_summary",
    ]

    @admin.action(description="Show Daily Payment Summary")
    def daily_payment_summary(self, request, queryset):

        summary = (
            Transaction.objects
            .values("created_at__date")
            .annotate(
                total_payments=Count("id"),
                total_amount=Sum("amount")
            )
            .order_by("-created_at__date")
        )

        for item in summary:
            date = item["created_at__date"]
            total_payments = item["total_payments"]
            total_amount = item["total_amount"]

            self.message_user(
                request,
                f"Date: {date} | "
                f"Payments: {total_payments} | "
                f"Total Amount: {total_amount}",
                messages.SUCCESS
            )