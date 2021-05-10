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

class Bovine(models.Model):
    """
    """
    name = models.CharField(max_length=128, blank=True)
    weight = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True)
    date_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    image = models.ImageField(blank= True,upload_to="bovinos/")

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bovine'
        verbose_name_plural = 'Bovines'

    def __str__(self):
        return self.name

