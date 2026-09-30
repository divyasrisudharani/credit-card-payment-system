from pydantic import BaseModel, Field


class PaymentRequest(BaseModel):
    card_id: int
    amount: float = Field(gt=0)