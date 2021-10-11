from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200, db_index=True)
    short_title = models.CharField('Краткий заголовок', max_length=200)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')
    place_id = models.CharField('Идентификатор места', max_length=200)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField('Изображение')
    position = models.IntegerField('Порядок следования', db_index=True)

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = ['position']
