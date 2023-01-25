from django.shortcuts import render, redirect
from .models import Post,Reply
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def main(request):
    posts= Post.objects.all()
    replys=Reply.objects.all()
    ctx={
        'posts':posts,
        'replys':replys,
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

@csrf_exempt #csrf 해제 시킴 (보안쪽)
def reply(request):
    jsonObject=json.loads(request.body)
    post_id=jsonObject['id']
    print(post_id)
    post=Post.objects.get(id=post_id)
    reply =Reply.objects.create(
        bord=post,
        member='member',
        content=jsonObject.get('comment'),
    )
    content=reply.content

    return JsonResponse({'content': content, 'id': post_id})

    jsonObject=json.loads(request.body)
    post_id=jsonObject['id']
    print(post_id)
    post=Post.objects.get(id=post_id)
    reply =Reply.objects. create(
        bord=post,
        member='member',
        content=jsonObject.get('comment'),
    )
    reply.save()

    ctx={
        'name':reply.member,
        'content':reply.content,
        'createDate' :reply.createDate,
        'updateDate' :reply.updateeDate,
        }
    return JsonResponse(ctx)

@csrf_exempt
def reply_del(request):
    req = json.loads(request.body)
    reply_id = req['id']

    comment = Reply.objects.get(id=reply_id)
    comment.delete()

    return JsonResponse({'id': reply_id})