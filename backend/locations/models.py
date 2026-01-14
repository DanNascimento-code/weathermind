from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        parts = [self.city]
        if self.region:
            parts.append(self.region)
        parts.append(self.country)
        return ", ".join(parts)