from django.db import models

class Jugador(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en gramos")
    picture = models.ImageField(upload_to='picture_players')
    position = models.CharField(max_length=60)
    

    def __str__(self):
        return self.name


class Entrenador(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)
    rut = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Equipo(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Nomina(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    time = models.CharField(max_length=5)



    def __str__(self):
        return self.name