from typing import Any, Dict

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


def handler_404(request, exception):
    template = loader.get_template('post_404.html')
    return HttpResponse(template.render({'exception': exception}, request), status=404) 


class PostList(ListView):
    queryset = Post.objects.select_related('author')
    paginate_by = 2
    template_name = 'post_pagination.html'
    ordering = 'id'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(PostList, self).get_context_data(**kwargs)
        context['new_post_form'] = PostForm()
        return context

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():

            new_post = Post.objects.create(
                content = form.cleaned_data['content'],
                author = request.user
            )
            new_post.save()
        else:
            print(form.errors)
        return self.get(request)


def post_feed(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = add_post(request)
    template = loader.get_template('feed.html')
    posts = Post.objects.select_related('author')
    return HttpResponse(template.render({'posts': posts, 'new_post_form': post_form}, request))


def post_detail(request, post_id):
    template = loader.get_template('post_detail.html')
    post = get_object_or_404(Post, id=post_id)
    return HttpResponse(template.render({'post': post}, request))

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
        
            new_post = Post.objects.create(
                content = form.cleaned_data['content'],
                author = request.user
            )
            new_post.save()
        else:
            print(form.errors)
        return form
