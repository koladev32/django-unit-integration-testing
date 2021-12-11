from __future__ import annotations

from typing import Optional

from django.conf import settings
import requests


class PaymentAPI:
    API_URL = None

    def __init__(self):
        if settings.ENV in ['PROD']:
            self.API_URL = settings.REAL_PAYMENT_API
        else:
            self.API_URL = settings.FAKE_PAYMENT_API

    def request_payment(self, cart_id: int, amount: int | float) -> Optional[dict]:

        data = {
            "cart_id": cart_id,
            "amount": amount
        }

        response = requests.post(f"http://{self.API_URL}/request_payment", json=data)

        return response.json()
