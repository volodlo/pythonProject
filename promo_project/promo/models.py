from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Person(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name ='Пользователь'
        verbose_name_plural = 'Пользователи'


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    houses = models.ManyToManyField('House')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Кампания'
        verbose_name_plural = 'Кампании'


class House(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    entrances = models.PositiveIntegerField()
    apartments_per_entrance = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.city}, {self.street}, {self.number}"

    class Meta:
        verbose_name ='Дом'
        verbose_name_plural = 'Дома'

class CustomUser(AbstractUser):
    # Добавьте новые поля
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True,
                                              verbose_name='user permissions')

    def __str__(self):
        return self.username