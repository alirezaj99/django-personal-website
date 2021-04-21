from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from site_about_us.models import AboutUs
from .models import Blogs, Comment
from .forms import CommentForm
from site_blog_category.models import BlogsCategory


class BlogsList(ListView):
    template_name = "blog/blog_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Blogs.objects.get_active_blogs().order_by("-id")


class BlogsListCategory(ListView):
    template_name = "blog/blog_list.html"
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = BlogsCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه ی مورد نظر یافت نشد")
        return Blogs.objects.get_blogs_by_category(category_name)

    def get_context_data(self, **kwargs):
        category_name = self.kwargs["category_name"]
        category = BlogsCategory.objects.filter(name__iexact=category_name).first()
        context = super().get_context_data(**kwargs)
        context["category"] = category

        return context


def blog_detail(request, *args, **kwargs):
    blog_id = kwargs["blogId"]
    blogs = Blogs.objects.get_by_id(blog_id)
    if blogs is None or not blogs.active:
        raise Http404("بلاگی مورد نطر یافت نشد")
    about_us = AboutUs.objects.first()
    comment: Comment = Comment.objects.filter(blog_id=blog_id, active=True)
    comment_count = len(comment)
    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        name = comment_form.cleaned_data.get("name")
        email = comment_form.cleaned_data.get("email")
        text = comment_form.cleaned_data.get("text")
        Comment.objects.create(name=name, email=email, text=text, blog_id=blog_id)
        return HttpResponseRedirect(blogs.get_absolute_url())
    context = {
        "blogs": blogs,
        "about_us": about_us,
        "comment": comment,
        "comment_form": comment_form,
        "comment_count": comment_count,

    }
    return render(request, "blog/blog_detail.html", context)


def blogs_category_partial(request):
    categories = BlogsCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "blog/blogs_category_partial.html", context)


def like(request, *args, **kwargs):
    blog_id = kwargs["blogId"]
    post = Blogs.objects.get(id=blog_id)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            return HttpResponse("you are like this post!")
        post.like.add(user)
        return redirect(Blogs.objects.get_by_id(blog_id))
    # todo: redirect to login page


def unlike(request, *args, **kwargs):
    blog_id = kwargs["blogId"]
    post = Blogs.objects.get(id=blog_id)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            post.like.remove(user)
            return redirect(Blogs.objects.get_by_id(blog_id))
        else:
            return HttpResponse("you are not like this post!")
    # todo: redirect to login page
