from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def total_value(self):
        orders = self.orders.all()
        return sum(order.total_value for order in orders if order.order_type == 'BUY') - \
                sum(order.total_value for order in orders if order.order_type == 'SELL')