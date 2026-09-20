from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_LIMIT = 5


def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    posts = get_published_posts()[:POSTS_LIMIT]
    return render(request, "blog/index.html", {"posts": posts})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = get_published_posts().filter(category=category)
    return render(
        request,
        "blog/category.html",
        {"category": category, "posts": posts},
    )


def post_detail(request, id):
    post = get_object_or_404(get_published_posts(), id=id)
    return render(request, "blog/detail.html", {"post": post})
