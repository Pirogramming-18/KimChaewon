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
    devtools = ToolList.objects.all()
    if request.method == "POST":
        devtool_id = request.POST["devtool"]        
        Post.objects.create(
            title=request.POST["title"],
            devtool=ToolList.objects.get(id=devtool_id),
            interest=request.POST["interest"],
            content=request.POST["content"],
            image=request.FILES["image"],
        )
        return redirect("/")
    context={
        "devtools": devtools,
    }
    return render(request, "posts/i_create.html",context=context)


def i_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    devtools = ToolList.objects.all()
    
    if request.method == "POST":
        devtool=request.GET.get("devtool.id")
        devtool_id = request.POST.get("devtool")
        post.title=request.POST["title"]
        post.devtool=ToolList.objects.get(id=devtool_id),
        post.interest=request.POST["interest"]
        post.content=request.POST["content"]
        if devtool_id:
            post.image=request.FILES.get("image")
        post.save()
        return redirect(f"/posts/{post.id}")
    context={
        "post":post,
        'devtools' : devtools,        
    }
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

def t_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        tool = ToolList.objects.get(id=pk)
        tool.delete()
    return redirect("/posts/tool")

def t_create(request):
    if request.method == "POST":
        ToolList.objects.create(
        name=request.POST["name"],
        kind=request.POST["kind"],
        content=request.POST["content"],
        )
        return redirect("/posts/tool")
    return render(request, "posts/t_create.html")

def t_update(request:HttpRequest, pk, *args, **kwargs):
    tool = ToolList.objects.get(id=pk)
    context={
        "tool":tool,
    }
    if request.method == "POST":
        tool.name=request.POST["name"]
        tool.kind=request.POST["kind"]
        tool.content=request.POST["content"]
        tool.save()
        return redirect(f"/posts/tool/{tool.id}")
    return render(request, "posts/t_update.html", context=context)