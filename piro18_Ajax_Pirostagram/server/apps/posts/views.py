from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def main(request):
    posts= Post.objects.all()
    ctx={
        'posts':posts,
    }
    return render(request, 'posts/main.html', ctx)

@csrf_exempt #csrf 해제 시킴 (보안쪽)
def like_ajax(request): 
    req=json.loads(request.body) #파이썬으로 형식 변경
    post_id=req['id']
    button_type=req['type']

    post=Post.objects.get(id=post_id)

    if button_type =='like':
        post.like+=1
    post.save()

    return JsonResponse({'id':post_id,'type':button_type})