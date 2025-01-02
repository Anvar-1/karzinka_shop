from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'