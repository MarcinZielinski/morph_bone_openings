from django.db import models


# Create your models here.
class XRay(models.Model):
    xRayImg = models.ImageField(upload_to='images/')
