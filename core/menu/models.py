from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Наименование блюда')
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=('menu_images/%Y/%M/%D'), blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=15000,
        decimal_places=2,
        verbose_name='Цена')
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    menu = models.ManyToManyField(MenuItem)
    name = models.CharField(max_length=25, verbose_name='Ваше имя')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.name
