from django.shortcuts import render,redirect
from .models import Post

def i_list(request):
    post_list=Post.objects.order_by('title')
    context={'post_list':post_list}
    return render(request,"posts/i_list.html",context=context)

    # posts = Post.objects.all()
    # text = request.GET.get("text")
    # if text:
    #     posts = posts.filter(content__contains=text)
        
    # return render(request, "posts/i_list.html", {"posts":posts})

def i_detail(request,pk,*args, **kwargs):
    post = Post.objects.get(id=pk)
    context={
        "post_id": post,
    }
    return render(request, "posts/i_detail.html", context=context)

def i_create(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            devtool=request.POST["devtool"],
            interest=request.POST["interest"],
            content=request.POST["content"],
            image=request.FILES["image"],
        )
        return redirect("/")
    return render(request, "posts/i_create.html")


def i_update(request):
    post_list=Post.objects.order_by('title')
    context={'post_list':post_list}
    return render(request,"posts/i_list.html",context)