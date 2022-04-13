from django.shortcuts import render, redirect
from .models import Blog, Comment



# Create your views here.
def blog(request):
    blogs = Blog.objects.order_by('-date')[:5]
    param={'blogs':blogs}
    print(param)
    return render(request,'blog/blog.html',param)
    

def create_blog(request):
    if request.method == "POST":
        _title = request.POST.get('title')
        _description = request.POST.get('description')
        _content=request.POST.get('content')
        if _title =='':
            return render(request,'blog/create_blog.html', {'error_message': ' The title is not empty. '})
        else:
            blog = Blog(title =_title, description = _description,content=_content )
            blog.save()
            return redirect('blog:blog')
    else:
        return render(request,'blog/create_blog.html')

def blog_i(request, id):
    
    blog = Blog.objects.get(pk=id)
    comments = blog.comments.all().order_by('-date')[:10]
    param={'comments':comments,'blog':blog,}
    if request.method == "POST":
       
        _name = request.POST.get('your_name')
        _comment=request.POST.get('comment')
        
        if _name =='' or _comment=='':
            return render(request,'blog/blog_i.html',{'error_message': ' The \"Your name\" or \"comment\" is not empty. '},param)
        else:
            comment_new = Comment(id_blog=blog, name = _name, comment = _comment)
            comment_new.save()
            return render(request,'blog/blog_i.html',param)
    return render(request,'blog/blog_i.html',param)

def update_blog(request,id):
    if request.method == "POST":
        _title = request.POST.get('title')
        _description = request.POST.get('description')
        _content=request.POST.get('content')
        if _title =='':
            return render(request,'blog/update_blog.html', {'error_message': ' The title is not empty. '})
        else:
            blog = Blog.objects.get(pk=id)
            blog.title=_title
            blog.description=_description
            blog.content=_content
            blog.save()
            blog_id= Blog.objects.get(pk=id)
            new_blog={'blog':blog_id}
            return render(request,'blog/blog_i.html',new_blog)
    else:
        return render(request,'blog/update_blog.html')

def delete_blog(request,id):
    blog=Blog.objects.filter(pk=id).delete()
    return redirect('blog:blog')
