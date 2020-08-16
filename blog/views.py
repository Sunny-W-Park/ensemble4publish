from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db import models, transaction
from django.db.models import F

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View, DetailView

from .forms import OrderForm  #CommentForm
from blog.forms import OrderForm  #CommentForm
from blog.models import Post, Order, Product  #Comment

from hitcount.views import HitCountDetailView, HitCountMixin

def blog_index(request):
    posts = Post.objects.all().order_by("title")
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
                    'title'
                    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = OrderForm()
    post.click

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                post = Post.objects.get(pk=pk)
                order = Order(
                sender = form.data.get('sender'),
                author = form.data.get('author'),
                quantity = form.data.get('quantity'),
                email = form.data.get('email'),
                phone = form.data.get('phone'),
                message_store = form.data.get('message_store'),
                signature = form.data.get('signature'),
                post = post
                )
            order.save()

            post.call += int(form.data.get('quantity'))
            post.save()
        return render(request, 'SubmitOK.html')
    orders = Order.objects.filter(post=post).order_by('-created_on')
    order_count = orders.count()
    context = {"post": post, "orders": orders, "form": form, "order_count": order_count,}
    return render(request, "blog_detail.html", context)

def blog_submit(request):
    return render(request, "SubmitOK.html")



class PostMixinDetailView(object):
    model = Post

class PostDetailView(PostMixinDetailView, HitCountDetailView):
    pass

class PostCountHitDetailView(HitCountDetailView):
    count_hit = True


#*****HitCount*****
#try:
#    hits = HitCount.objects.get(ip=ip, post=post)
#except Exception as e:
#    print(e)
#    Post.objects.filter(attachment_ptr_id = post_id).update(hits=post.hits +1)
#    hits.save()
#else:
#    if not hits.date == timezone.now().date():
#        Post.objects.filter(attachment_ptr_id = post_id).update(hits=post.hits +1)
#        hits.date = timezone.now()
#        hits.save()
#    else:
#        print(str(ip) + 'has already hit this post. \n\n')


#def form_valid(form):
#    with transaction.atomic():
#        post = Post.objects.get(pk=pk)
#        order = Order(
#                sender = form.data.get('sender'),
#                author = form.data.get('author'),
#                quantity = form.data.get('quantity'),
#                email = form.data.get('email'),
#                phone = form.data.get('phone'),
#                message_store = form.data.get('message_store'),
#                post = post
#                )
#        order.save()
# 
#        post.call += int(form.data.get('quantity'))
#        post.save()
#    return super().form_valid(form)


##### Original Orderview #####


#def blog_detail(request, pk):
#    post = Post.objects.get(pk=pk)
#    form = OrderForm()
#
#    if request.method == "POST":
#       form = OrderForm(request.POST)
#       if form.is_valid():
#                order = Order(
#                   sender  = form.cleaned_data["sender"],
#                   author = form.cleaned_data["author"],
#                   quantity  = form.cleaned_data["quantity"],
#                   email = form.cleaned_data["email"],
#                   phone = form.cleaned_data["phone"],
#                   message_store = form.cleaned_data["message_store"],
#                   post=post,
#                   )
#                order.save()
#                return redirect("/blog/")
#
#    orders = Order.objects.filter(post=post).order_by('-created_on')
#    order_count = orders.count()
#    context = {"post":post, "orders":orders, "form":form, "order_count":order_count,}
#    return render(request, "blog_detail.html", context)

