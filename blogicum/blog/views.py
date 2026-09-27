from django.shortcuts import get_object_or_404, render

from .models import Category, Post

POSTS_LIMIT = 5


def index(request):
    posts = Post.objects.published()[:POSTS_LIMIT]
    return render(request, "blog/index.html", {"posts": posts})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = (
        Post.objects.published()
        .filter(category=category)
        .select_related("author", "location")
    )
    return render(
        request,
        "blog/category.html",
        {"category": category, "posts": posts},
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.published(), pk=post_id)
    return render(request, "blog/detail.html", {"post": post})
