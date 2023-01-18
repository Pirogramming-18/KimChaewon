from django.db import models
from django.utils import timezone


class ToolList(models.Model):
    name=models.CharField(max_length=64)
    kind=models.CharField(max_length=64)
    content = models.TextField()

class Post(models.Model):
    title=models.CharField(max_length=64)
    devtool= models.ForeignKey(ToolList, on_delete=models.CASCADE)
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest=models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now) #만들어진 시간
