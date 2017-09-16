from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

import blog
from .models import Post, Like, Tag
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy
from .forms import PostForm, ActivityPostForm
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

def post_spot_list(request, tag=None): #tag없이 request만 올 수도 있고, tag있이 검색해서 올 수도 있음.

    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    tag_all = Tag.objects.annotate(num_post=Count('post')).order_by('-num_post')  # 가장 인기 많은 태그를 나타내기 위함
    # Tag 별로 post의 숫자를 계산해서, post가 많은 태그 순으로 tag_all에 들어간다(Category 상관 없이)
    spotposts = Post.objects.filter(postcategory="SPOT")

    if tag:#tag_set의 name이 tag인 것..(tag_set이 있다면 tag)??iexact:대소문자 상관없이 검색
        spotposts = spotposts.filter(tag_set__name__iexact=tag) \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            spotposts = spotposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            spotposts = spotposts.order_by('-created_date')
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

    else:
        spotposts = spotposts.all() \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            spotposts = spotposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            spotposts = spotposts.order_by('-created_date')
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_spot_list.html', {'spotposts': spotposts, 'tag': tag, 'tag_all': tag_all})

def post_spot_detail(request, pk):
    spotpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_spot_detail.html', {'spotpost': spotpost})

def post_accomodation_list(request, tag=None):
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    tag_all = Tag.objects.annotate(num_post=Count('post')).order_by('-num_post')  # 가장 인기 많은 태그를 나타내기 위함
    # Tag 별로 post의 숫자를 계산해서, post가 많은 태그 순으로 tag_all에 들어간다(Category 상관 없이)
    accomodationposts = Post.objects.filter(postcategory="ACCOMODATION")

    if tag:  # tag_set의 name이 tag인 것..(tag_set이 있다면 tag)??iexact:대소문자 상관없이 검색
        accomodationposts = accomodationposts.filter(tag_set__name__iexact=tag) \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            accomodationposts = accomodationposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            accomodationposts = accomodationposts.order_by('-created_date')
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})

    else:
        accomodationposts = accomodationposts.all() \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            accomodationposts = accomodationposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            accomodationposts = accomodationposts.order_by('-created_date')
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_accomodation_list.html', {'accomodationposts': accomodationposts, 'tag': tag, 'tag_all': tag_all})


def post_accomodation_detail(request, pk):
    accomodationpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_accomodation_detail.html', {'accomodationpost': accomodationpost})

def post_restaurant_list(request, tag=None):

    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    tag_all = Tag.objects.annotate(num_post=Count('post')).order_by('-num_post')  # 가장 인기 많은 태그를 나타내기 위함
    # Tag 별로 post의 숫자를 계산해서, post가 많은 태그 순으로 tag_all에 들어간다(Category 상관 없이)
    restaurantposts = Post.objects.filter(postcategory="RESTAURANT")

    if tag:  # tag_set의 name이 tag인 것..(tag_set이 있다면 tag)??iexact:대소문자 상관없이 검색
        restaurantposts = restaurantposts.filter(tag_set__name__iexact=tag) \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            restaurantposts = restaurantposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            restaurantposts = restaurantposts.order_by('-created_date')
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

    else:
        restaurantposts = restaurantposts.all() \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            restaurantposts = restaurantposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            restaurantposts = restaurantposts.order_by('-created_date')
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_restaurant_list.html', {'restaurantposts': restaurantposts, 'tag': tag, 'tag_all': tag_all})

def post_restaurant_detail(request, pk):
    restaurantpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_restaurant_detail.html', {'restaurantpost': restaurantpost})

def post_activity_list(request, tag=None): #tag없이 request만 올 수도 있고, tag있이 검색해서 올 수도 있음.

    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    tag_all = Tag.objects.annotate(num_post=Count('post')).order_by('-num_post')  # 가장 인기 많은 태그를 나타내기 위함
    # Tag 별로 post의 숫자를 계산해서, post가 많은 태그 순으로 tag_all에 들어간다(Category 상관 없이)
    activityposts = Post.objects.filter(postcategory="ACTIVITY")

    if tag:#tag_set의 name이 tag인 것..(tag_set이 있다면 tag)??iexact:대소문자 상관없이 검색
        activityposts = activityposts.filter(tag_set__name__iexact=tag) \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            activityposts = activityposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            activityposts = activityposts.order_by('-created_date')
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

    else:
        activityposts = activityposts.all() \
            .prefetch_related('tag_set', 'like_user_set')
        if sort == 'likes':
            activityposts = activityposts.annotate(count=Count('like_user_set')).order_by(
                '-count')
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

        elif sort == 'date':
            activityposts = activityposts.order_by('-created_date')
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

        else:
            return render(request, 'blog/post_activity_list.html', {'activityposts': activityposts, 'tag': tag, 'tag_all': tag_all})

def post_activity_detail(request, pk):
    activitypost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_activity_detail.html', {'activitypost': activitypost})
'''
def post_recreation_list(request):
    recreationposts = Post.objects.filter(postcategory="RECREATION")
    return render(request, 'blog/post_recreation_list.html', {'recreationposts': recreationposts})

def post_recreation_detail(request, pk):
    recreationpost = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_recreation_detail.html', {'recreationpost': recreationpost})
'''

@login_required()
def post_new(request): #request 객체안의 request.POST는 우리가 입력했던 데이터를 가지고 있음
    if request.method == "POST":
        print(request.FILES)
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            post.tag_save()
            messages.info(request, '새 글이 등록되었습니다.')
            if post.postcategory == "SPOT":
                return redirect('post_spot_detail', pk=post.pk)

            elif post.postcategory == "ACCOMODATION":
                return redirect('post_accomodation_detail', pk=post.pk)

            #elif post.postcategory == "RECREATION":
                #return redirect('post_recreation_detail', pk=post.pk)

            else:
                return redirect('post_restaurant_detail', pk=post.pk)
        else : 
            return redirect('post_activity_list')

    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required()
def post_activity_new(request):
    if request.method =="POST":
        form = ActivityPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            post.tag_save()
            messages.info(request, '새 글이 등록되었습니다.')
            if post.postcategory == "ACTIVITY":
                return redirect('post_activity_detail', pk=post.pk)
    else:
        form = ActivityPostForm()
    return render(request, 'blog/post_activity_new.html', {'form':form})

@login_required()
def post_spot_edit(request, pk):
    spotpost = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        if spotpost.owner == User.objects.get(username = request.user.get_username()):
            form = PostForm(request.POST, instance=spotpost)
            if form.is_valid():
                spotpost = form.save(commit=False)
                spotpost.owner = request.user
                spotpost.created_date = timezone.now()
                spotpost.save()
                spotpost.tag_save()
                return redirect('post_spot_detail', pk=spotpost.pk)
    else:
        form = PostForm(instance=spotpost)
    return render(request, 'blog/post_spot_edit.html', {'form': form})

@login_required()
def post_accomodation_edit(request, pk):
    accomodationpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if accomodationpost.owner == User.objects.get(username = request.user.get_username()):
            form = PostForm(request.POST, instance=accomodationpost)
            if form.is_valid():
                accomodationpost = form.save(commit=False)
                accomodationpost.owner = request.user
                accomodationpost.created_date = timezone.now()
                accomodationpost.save()
                accomodationpost.tag_save()
                return redirect('post_spot_detail', pk=accomodationpost.pk)
    else:
        form = PostForm(instance=accomodationpost)
    return render(request, 'blog/post_accomodation_edit.html', {'form': form})

@login_required()
def post_restaurant_edit(request, pk):
    restaurantpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if restaurantpost.owner == User.objects.get(username = request.user.get_username()):
            form = PostForm(request.POST, instance=restaurantpost)
            if form.is_valid():
                restaurantpost = form.save(commit=False)
                restaurantpost.owner = request.user
                restaurantpost.created_date = timezone.now()
                restaurantpost.save()
                restaurantpost.tag_save()
            return redirect('post_restaurant_detail', pk=restaurantpost.pk)
    else:
        form = PostForm(instance=restaurantpost)
    return render(request, 'blog/post_restaurant_edit.html', {'form': form})

@login_required()
def post_activity_edit(request, pk):
    activitypost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if activitypost.owner == User.objects.get(username = request.user.get_username()):
            form = ActivityPostForm(request.POST, instance=activitypost)
            if form.is_valid():
                activitypost = form.save(commit=False)
                activitypost.owner = request.user
                activitypost.created_date = timezone.now()
                activitypost.save()
                activitypost.tag_save()
            return redirect('post_activity_detail', pk=activitypost.pk)
    else:
        form = ActivityPostForm(instance=activitypost)
    return render(request, 'blog/post_activity_edit.html', {'form': form})

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

@login_required()
def post_spot_delete(request, pk):
    spotpost = get_object_or_404(Post, pk=pk)
    if spotpost.owner == User.objects.get(username = request.user.get_username()):
        spotpost.delete()
        return redirect('post_spot_list')
    else:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_spot_list')

@login_required()
def post_accomodation_delete(request, pk):
    accomodationpost = get_object_or_404(Post, pk=pk)
    if accomodationpost.owner == User.objects.get(username=request.user.get_username()):
        accomodationpost.delete()
        return redirect('post_accomodation_list')
    else:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_accomodation_list')


@login_required()
def post_restaurant_delete(request, pk):
    restaurantpost = get_object_or_404(Post, pk=pk)
    if restaurantpost.owner == User.objects.get(username=request.user.get_username()):
        restaurantpost.delete()
        return redirect('post_restaurant_list')
    else:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_restaurant_list')

@login_required()
def post_activity_delete(request, pk):
    activitypost = get_object_or_404(Post, pk=pk)
    if activitypost.owner == User.objects.get(username=request.user.get_username()):
        activitypost.delete()
        return redirect('post_activity_list')
    else:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_activity_list')


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm #내장 회원가입 폼을 커스터마이징 한 것을 사용함
    success_url = reverse_lazy('create_user_done')

class UsercreateDoneTV(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
