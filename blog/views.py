from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from pip._vendor.requests import post

from blog.models import Post, Comment


def Home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()
    for i in posts:
       i.content = i.content[0:100] + "....."
    context = {'object_list': posts}
    return render(request,template_name,context)


def post_detail(request, pk):
    template_name = 'blog/post.html'
    post = Post.objects.get(id=int(pk))
    comments = Comment.objects.filter()
    context = {'post' : post, 'comments' : comments}
   # if request.comment_text == "POST":
    #    comment_text = Comment()

    return render(request, template_name,context)

def add_post(request):
    if request.method == "POST" :
       title = request.POST['title']
       content = request.POST['content']
       img = request.FILES['img']
       is_published =request.POST['is_published']
       user = User.objects.get(username=request.user.username)
       new_post = Post(title=title, content=content, img= img, is_published=is_published, user= user)
       new_post.save()
       return redirect('post', new_post.id)
    else:
        template_name = 'blog/add_post.html'
        context = {}
        return render(request, template_name, context)

def edit_post(request, pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username != post.user.username:
        raise PermissionDenied
        #permission denied
    if request.method == "GET":
        template_name = 'blog/edit_post.html'
        context = {'post': post}
        return render(request, template_name,context)
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        if 'img' in request.FILES:
            post.img = request.FILES["img"]
        if 'is published' in request.POST:
            post.is_published = request.POST['is_published']
        post.save()
        return redirect('post', post.id)

def del_post(request,id):
    if Post.objects.get(id=id) is not None:
        post = Post.objects.get(id=id)
        if post.user.username == request.user.username:
            post.delete()
            return redirect('Home')
    raise PermissionDenied



def signup(request):
    template = 'registration/signup.html'
    context = {}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.filter(email=email)
        if len(user) != 0:
            context['error'] = "Email is already taken"
            return redirect(request, template, context)
            user = User.objects.filter(username=username)
        if len(user) != 0:
            context['error'] = "User name already taken"
            return redirect(request, template, context)
        if password1 == password2:
            user = User(first_name = firstname, last_name = lastname, username = username, email = email)
            user.set_password(password1)
            user.save()
        return redirect('login')
    return render(request, template, context)

"""class AddPost(generic.CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    success_url = '/blog'
    fields = ['title', 'content', 'img' ,'is_published', 'user']

class EditPost(generic.UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'content', 'img', 'is_published', 'user']
"""