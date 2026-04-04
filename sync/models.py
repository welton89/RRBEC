from django.db import models

class ChangeLog(models.Model):
    MODEL_CHOICES = [
        ('Product', 'Product'),
        ('Comanda', 'Comanda'),
        ('Order', 'Order'),
        ('Client', 'Client'),
        ('Categories', 'Categories'),
        ('Mesa', 'Mesa'),
        ('Payments', 'Payments'),
    ]
    ACTION_CHOICES = [
        ('SAVE', 'Save'),
        ('DELETE', 'Delete'),
    ]
    
    model_name = models.CharField(max_length=50, choices=MODEL_CHOICES)
    object_id = models.IntegerField()
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['model_name', 'object_id']),
        ]

    def __str__(self):
        return f"{self.model_name} {self.object_id} {self.action} at {self.timestamp}"
