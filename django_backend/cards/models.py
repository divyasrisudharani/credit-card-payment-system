from django.db import models

# Create your models here.
from django.db import models


class CreditCard(models.Model):
    card_holder_name = models.CharField(max_length=100)
    masked_card_number = models.CharField(max_length=19)
    last_four_digits = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card_holder_name} - ****{self.last_four_digits}"