from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    descriptions = models.CharField(max_length=255, verbose_name="Описание", blank=True, null=True)
    logo = models.ImageField(upload_to='geeks_logo/',verbose_name="Логотип", blank=True, null=True)
    image = models.ImageField(upload_to='geeks_image/', verbose_name='Фотография', blank=True, null=True)
    image_2 = models.ImageField(upload_to='geeks_image/', verbose_name='Фотография', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основная Настройка",
        verbose_name_plural = "Основные Настройки"

class Gallery(models.Model):
    image = models.ImageField(
        upload_to="gallery_image",
        verbose_name="Фотография для галлери"
    )
    class Meta:
        verbose_name = "Галерея",
        verbose_name_plural = "Галерея"

class Contact(models.Model):
    phone = models.CharField(max_length=30, verbose_name="Телефонный номер")
    instagram = models.URLField(verbose_name="инстаграмм")
    whatsapp = models.URLField(verbose_name="ватсап")
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакт",
        verbose_name_plural = "Контакты"
