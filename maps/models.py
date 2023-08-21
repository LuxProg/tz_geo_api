from django.db import models


class TblAzs(models.Model):
    id = models.IntegerField(name='id', primary_key=True, verbose_name='ID')
    road_code = models.IntegerField(blank=False, verbose_name='Код дороги')
    geomtype = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип фигуры')
    coordinates = models.TextField(blank=True, null=True, verbose_name='Координаты')

    # для удобного описания в админке
    def __str__(self):
        return f'АЗС №{self.id}'

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'
        db_table = 'tbl_azs'


class TblRoads(models.Model):
    road_code = models.IntegerField(verbose_name='Код дороги', primary_key=True, default=1)
    name = models.CharField(verbose_name='Наименование дороги', max_length=100, blank=True, null=True)
    length_km = models.FloatField(verbose_name='Протяженность', blank=True, null=True)
    geomtype = models.CharField(verbose_name='Тип фигуры', max_length=50, blank=True, null=True)
    coordinates = models.TextField(verbose_name='Список координат', blank=True, null=True)

    def __str__(self):
        return f'Дорога {self.name}'

    class Meta:
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'
        db_table = 'tbl_roads'
