
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорія"
        verbose_name_plural = "КатегоріЇ"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Зображення")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Знижка %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return f'{self.name} Кількість - {self.quantity}'  
