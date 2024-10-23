from django.db import models

class FootbalArea(models.Model):
    area_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    grass_type = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='football_areas/', blank=True, null=True)

    def __str__(self):
        return self.area_name