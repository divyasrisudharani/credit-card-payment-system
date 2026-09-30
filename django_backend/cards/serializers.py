from rest_framework import serializers
from .models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = [
            "id",
            "card_holder_name",
            "masked_card_number",
            "last_four_digits",
            "created_at",
        ]