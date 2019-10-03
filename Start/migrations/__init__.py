from django.db import models

class Complain(models.Model):
    title=models.CharField(max_length=36)