from django.db import models
#a
class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)