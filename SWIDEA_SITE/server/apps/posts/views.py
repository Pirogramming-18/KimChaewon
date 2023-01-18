from django.shortcuts import render,redirect
from server.apps.posts.models import Post, ToolList
from django.http.request import HttpRequest

def i_list(request:HttpRequest,*args, **kwargs):
    
    sort_option = request.GET.get('sort')
    print(sort_option)

    if sort_option:
        if sort_option=='byname':
            post_list=Post.objects.order_by('title')
        elif sort_option=='register':
            post_list=Post.objects.order_by('timestamp')
        elif sort_option=='newest':
            post_list=Post.objects.order_by('-timestamp')
        # elif sort_option=="pick":
        #     여기는 나중에 구현 해볼게여..
    else:
        post_list=Post.objects.all()

    context={
        'post_list':post_list
        }        
    return render(request,"posts/i_list.html",context=context)


def i_detail(request:HttpRequest,pk,*args, **kwargs):
    post = Post.objects.get(id=pk)
    print(post)
    context={
        "post": post,
    }
    return render(request, "posts/i_detail.html", context=context)

def i_create(request):
    tool_list=Post.TOOL_CHOICE
    context={
        "tool_list":tool_list,
    }
    if request.method == "POST":
        
        Post.objects.create(
            title=request.POST["title"],
            devtool=request.POST["devtool"],
            interest=request.POST["interest"],
            content=request.POST["content"],
            image=request.FILES["image"],
        )
        return redirect("/")
    return render(request, "posts/i_create.html",context=context)


def i_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    tool_list=Post.TOOL_CHOICE
    context={
        "post":post,
        "tool_list":tool_list,
    }
    if request.method == "POST":
        post.title=request.POST["title"]
        post.devtool=request.POST["devtool"]
        post.interest=request.POST["interest"]
        post.content=request.POST["content"]
        post.image=request.FILES.get("image")
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/i_update.html", context=context)

def i_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def t_list(request:HttpRequest,*args, **kwargs):
    tool_list=ToolList.objects.all()

    context={
        'tool_list':tool_list
        }        
    return render(request,"posts/t_list.html",context=context)

def t_detail(request:HttpRequest,pk,*args, **kwargs):
    tool= ToolList.objects.get(id=pk)
    context={
        "tool": tool,
    }
    return render(request, "posts/t_detail.html", context=context)
