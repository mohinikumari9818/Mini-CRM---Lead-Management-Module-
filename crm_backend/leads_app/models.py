from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    def __str__(self):
        return self.name
