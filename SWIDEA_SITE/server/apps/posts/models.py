from django.db import models
from django.utils import timezone


class ToolList(models.Model):
    name=models.CharField(max_length=64)
    kind=models.CharField(max_length=64)
    content = models.TextField()

class Post(models.Model):
    title=models.CharField(max_length=64)
    tool= models.ForeignKey(ToolList, on_delete=models.CASCADE)
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest=models.IntegerField(default=0)
    toollist=ToolList.objects.all()
    TOOL_CHOICE=[]
    for tooll in toollist:
        TOOL_CHOICE.append((tooll,tooll))
    devtool=models.CharField(max_length=64,choices=TOOL_CHOICE)
    timestamp = models.DateTimeField(default=timezone.now) #만들어진 시간
