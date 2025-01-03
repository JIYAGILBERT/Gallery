from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.MODEL):
    feedimage=models.ImageField(upload_to='/image')
