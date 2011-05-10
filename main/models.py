from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date uploaded')
    image_file = models.ImageField(upload_to='photos')
