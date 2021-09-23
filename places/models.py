from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    title_short = models.CharField('Краткий заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')
    place_id = models.CharField('Идентификатор места', max_length=200)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='image', verbose_name='Место')
    image = models.ImageField('Изображение')
    position = models.IntegerField('Порядок следования')

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = ['position']
