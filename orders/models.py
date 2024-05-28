from django.db import models
from django.conf import settings
from portfolios.models import Portfolio

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    ORDER_TYPES = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    ORDER_STATUS = (
        ('OPEN', 'Open'),
        ('FILLED', 'Filled'),
        ('CANCELLED', 'Cancelled'),
    )
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='PENDING')

    def __str__(self):
        return f"{self.get_order_type_display()} {self.quantity} {self.symbol} @ {self.price}"

    @property
    def total(self):
        return self.quantity * self.price