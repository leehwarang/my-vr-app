from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

import blog
from .models import Post, Like
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
try:
    from django.utils import simplejson as json
except ImportError:
    import json



#from .forms import UserForm
#from django.contrib.auth.models import User
#from django.contrib.auth import login

#from django.views.generic import ListView, DetailView, CreateView

def post_all(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_all.html', {'posts': posts})

def post_spot_list(request):
	spotposts = Post.objects.filter(postcategory="SPOT")
	return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts})

def post_spot_detail(request, pk):
    spotpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_spot_detail.html', {'spotpost': spotpost})

def post_accomodation_list(request):
	accomodationposts = Post.objects.filter(postcategory="ACCOMODATION")
	return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts})

def post_accomodation_detail(request, pk):
    accomodationpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_accomodation_detail.html', {'accomodationpost': accomodationpost})

def post_restaurant_list(request):
	restaurantposts = Post.objects.filter(postcategory="RESTAURANT")
	return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts})

def post_restaurant_detail(request, pk):
    restaurantpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_restaurant_detail.html', {'restaurantpost': restaurantpost})

def post_recreation_list(request):
    recreationposts = Post.objects.filter(postcategory="RECREATION")
    return render(request, 'blog/post_recreation_list.html', {'recreationposts': recreationposts})

def post_recreation_detail(request, pk):
    recreationpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_recreation_detail.html', {'recreationpost': recreationpost})


@login_required()
def post_new(request): #request 객체안의 request.POST는 우리가 입력했던 데이터를 가지고 있음
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.info(request, '새 글이 등록되었습니다.')
            if post.postcategory == "SPOT":
                return redirect('post_spot_detail', pk=post.pk)

            elif post.postcategory == "ACCOMODATION":
                return redirect('post_accomodation_detail', pk=post.pk)

            elif post.postcategory == "RECREATION":
                return redirect('post_recreation_detail', pk=post.pk)

            else:
                return redirect('post_restaurant_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required()
def post_spot_edit(request, pk):
    spotpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=spotpost)
        if form.is_valid():
            spotpost = form.save(commit=False)
            spotpost.author = request.user
            spotpost.created_date = timezone.now()
            spotpost.save()
            return redirect('post_spot_detail', pk=spotpost.pk)
    else:
        form = PostForm(instance=spotpost)
    return render(request, 'blog/post_spot_edit.html', {'form': form})

@login_required()
def post_accomodation_edit(request, pk):
    accomodationpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=accomodationpost)
        if form.is_valid():
            accomodationpost = form.save(commit=False)
            accomodationpost.author = request.user
            accomodationpost.created_date = timezone.now()
            accomodationpost.save()
            return redirect('post_spot_detail', pk=accomodationpost.pk)
    else:
        form = PostForm(instance=accomodationpost)
    return render(request, 'blog/post_accomodation_edit.html', {'form': form})

@login_required()
def post_restaurant_edit(request, pk):
    restaurantpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=restaurantpost)
        if form.is_valid():
            restaurantpost = form.save(commit=False)
            restaurantpost.author = request.user
            restaurantpost.created_date = timezone.now()
            restaurantpost.save()
            return redirect('post_restaurant_detail', pk=restaurantpost.pk)
    else:
        form = PostForm(instance=restaurantpost)
    return render(request, 'blog/post_restaurant_edit.html', {'form': form})

@login_required()
def post_recreation_edit(request, pk):
    recreationpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=recreationpost)
        if form.is_valid():
            recreationpost = form.save(commit=False)
            recreationpost.author = request.user
            recreationpost.created_date = timezone.now()
            recreationpost.save()
            return redirect('post_recreation_detail', pk=recreationpost.pk)
    else:
        form = PostForm(instance=recreationpost)
    return render(request, 'blog/post_recreation_edit.html', {'form': form})

@login_required()
@require_POST #해당 view는 POST method만 받는다
def post_like(request): #http가 서버에게 뭔가를 요청하는 것. 나 이 정보를 줘!
    pk = request.POST.get('pk', None) #사용자가 좋아요 버튼을 클릭한 post의 pk를 얻음
    post = get_object_or_404(Post, pk=pk) # ajax 통신을 통해서 template에서 POST방식으로 전달. pk를 가지고 있는 Post model을 전달
    post_like, post_like_created = post.like_set.get_or_create(user=request.user) #좋아요/이미 좋아요 받음(login한 사용자 정보를 가지고 옴)
    #post_like는 내가 검색하고자 하는 모델의 객체(object)이고, get_or_create(login한 user)에 의해 만들어졌다면 post_like_created는 참, 아니면 false

    if not post_like_created: #만약 이미 좋아요를 누른 상황이었다면(참일 때)
        post_like.delete() #좋아요 취소
        message = "좋아요 취소"

    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message,
               'username' : request.user.username
             }

    return HttpResponse(json.dumps(context), content_type="application/json")
    # context를 json 타입으로 data 전달


'''
def post_spot_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.owner != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_spot_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
        return redirect('post:post_spot_list')
  
def post_accomodation_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.owner != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_accomodation_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
        return redirect('post:post_accomodation_list')

def post_restaurant_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.owner != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_restaurant_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
        return redirect('post:post_restaurant_list')
'''


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm #내장 회원가입 폼을 커스터마이징 한 것을 사용함
    success_url = reverse_lazy('create_user_done')

class UsercreateDoneTV(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
