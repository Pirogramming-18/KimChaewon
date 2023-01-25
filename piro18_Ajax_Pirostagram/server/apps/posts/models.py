from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')


class Reply(models.Model):
    content = models.CharField(max_length=256)
    member=models.CharField(max_length=32)
    bord=models.ForeignKey(Post,on_delete=models.CASCADE)
    createDate=models.DateField(auto_now_add=True)
    updateeDate=models.DateField(auto_now=True)
