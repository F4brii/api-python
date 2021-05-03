from django.db import models

# Create your models here.
class Brand(models.Model):
    """
    """
    brand = models.CharField(max_length=128, blank=True)
    owner = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand