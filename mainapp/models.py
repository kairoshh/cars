from django.db import models

class CarMark(models.Model):
    name = models.CharField(max_length=127)
    date_created = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=126)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=125)
    color = models.CharField(max_length=123)
    year = models.PositiveIntegerField(default=0)
    max_speed =  models.PositiveIntegerField(default=0)
    horse_power = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    cars = models.ForeignKey(
        to=CarMark, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Class{self.name} - {self.car.name}'