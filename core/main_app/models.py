from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ваше имя')
    email = models.EmailField(verbose_name='Ваш email')
    description = models.TextField(verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обратный отзыв'
        verbose_name_plural = 'Обратные отзывы'

    def __str__(self) -> str:
        return self.name

class AboutRestaurant(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название ресторана')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    work_hours = models.TextField(verbose_name='Режим работы')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self) -> str:
        return self.name

class PhotoGallery(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='media/%Y/%M/%D')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class News(models.Model):
    name = models.CharField(max_length=150, verbose_name='Новости')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Конец акции')

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Наименование блюда')
    image = models.ImageField(verbose_name='Изображение', upload_to=('menu_images/%Y/%M/%D'))
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=15000, decimal_places=3, verbose_name='Цена')
    
    class Meta:
        verbose_name='Блюдо'
        verbose_name_plural='Блюда'

    def __str__(self) -> str:
        return self.name

class Feed_Back(models.Model):  #отзывы
    title = models.CharField(max_length=200, verbose_name='Оглавление')
    description = models.TextField(verbose_name='Описание')
    username = models.CharField(max_length=20, verbose_name='Ваше имя', blank=True)
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона', blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self) -> str:
        return self.title

class PaymentInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Оплата')
    description = models.TextField(verbose_name='Описание оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self) -> str:
        return self.name




