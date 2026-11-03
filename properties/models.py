
from django.db import models


class Property(models.Model):

    title = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    bedrooms = models.IntegerField()

    bathrooms = models.IntegerField()

    area = models.IntegerField()

    image = models.URLField(blank=True)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
