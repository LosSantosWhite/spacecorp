from django.db import models


class Artist(models.Model):
    name = models.CharField("Имя артиста", max_length=100)


class Album(models.Model):
    name = models.CharField("Название альбома", max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField("Год выпуска")

    def __str__(self):
        return f"{self.name}[{self.year}]"


class Track(models.Model):
    name = models.CharField("Название композиции", max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return self.name
