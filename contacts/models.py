from django.db import models


class Contact(models.Model):
    book = models.CharField(max_length=20)
    book_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
