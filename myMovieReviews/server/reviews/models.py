from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#별점 제한 모듈

# Create your models here.
class Movie(models.Model):
    #제목, 개봉 년도, 장르, 별점
    nameMv=models.CharField(max_length=64)
    yearsMv=models.CharField(max_length=32,help_text='개봉 년도')
    genreMv=models.CharField(max_length=32)
    gradeMv= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],help_text="0~5사이 값으로 입력하세요")
    


