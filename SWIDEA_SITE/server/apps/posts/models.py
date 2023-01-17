from django.db import models

class Post(models.Model):
    TOOL_CHOICE=[('django',"Django"),
    ('react','React'),
    ('spring','Spring'),
    ('node.js','Node.js'),
    ('java','Java'),
    ('c++','C++')
    ]
    title=models.CharField(max_length=64)
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest=models.IntegerField(default=0)
    devtool=models.CharField(max_length=64,choices=TOOL_CHOICE)

class ToolList(models.Model):
    name=models.CharField(max_length=64)
    kind=models.CharField(max_length=64)
    content = models.TextField()