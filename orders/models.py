from django.db import models

class Order(models.Model):
    datestart = models.DateTimeField()
    dateend = models.DateTimeField()

