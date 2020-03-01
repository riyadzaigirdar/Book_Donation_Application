from django.db import models


class Subscribe(models.Model):
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, max_length=254)

    def __str__(self):
        return f'subcribed by { self.name }'
