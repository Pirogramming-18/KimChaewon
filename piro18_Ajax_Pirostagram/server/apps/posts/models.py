from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')