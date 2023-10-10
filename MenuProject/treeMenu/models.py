from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    name = models.CharField('name', max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    is_cleaned = False
    name = models.CharField('name', max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['parent__pk']

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent:
            if self == self.parent:
                raise ValidationError('Parent to itself cannot be.')
            if self.menu != self.parent.menu:
                raise ValidationError('Parent must be from item menu.')
