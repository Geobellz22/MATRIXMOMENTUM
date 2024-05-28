from django.db import models

class Signal(models.Model):
    symbol = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Signal for {self.symbol}"
    
