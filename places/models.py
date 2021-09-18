from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField('Изображение')
    position = models.IntegerField('Порядок следования')

    def __str__(self):
        return f'{self.position} {self.place}'
