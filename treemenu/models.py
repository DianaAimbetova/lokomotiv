from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Scheme(MPTTModel):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name = 'children')
    chineese_name = models.CharField(max_length=50, blank=True, null=True)
    chapter = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.CharField(blank=True, null=True, max_length = 50)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Схема'
        verbose_name_plural = 'Схемы'
