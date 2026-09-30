import os
import sys
import random

from pathlib import Path

from fastapi import FastAPI
from schemas import PaymentRequest


# Connect FastAPI with Django
BASE_DIR = Path(__file__).resolve().parent.parent
DJANGO_DIR = BASE_DIR / "django_backend"

sys.path.append(str(DJANGO_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "django_backend.settings"
)

import django
django.setup()

from transactions.models import Transaction


app = FastAPI(title="Credit Card Payment System")


@app.get("/")
def home():
    return {
        "message": "Credit Card Payment API is running"
    }


@app.post("/payments")
def make_payment(payment: PaymentRequest):

    # Step 1: Create transaction with PENDING status
    transaction = Transaction.objects.create(
        card_id=payment.card_id,
        amount=payment.amount,
        status="PENDING"
    )

    # Step 2: Simulate payment
    payment_success = random.choice([True, False])

    # Step 3: Update final status
    if payment_success:
        transaction.status = "SUCCESS"
    else:
        transaction.status = "FAILED"

    transaction.save(update_fields=["status"])

    return {
        "transaction_id": transaction.id,
        "card_id": transaction.card_id,
        "amount": transaction.amount,
        "status": transaction.status
    }