from django.contrib import admin

# Register your models here.
from .models import CreditCard


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "card_holder_name",
        "masked_card_number",
        "last_four_digits",
        "created_at",
    )

    search_fields = (
        "card_holder_name",
        "last_four_digits",
    )

    ordering = (
        "-created_at",
    )