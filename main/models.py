from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date uploaded')
    image_file = models.ImageField(upload_to='photos')
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.title
