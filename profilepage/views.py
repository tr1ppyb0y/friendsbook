from django.http.response import HttpResponse
from django.template import loader

from .models import ProfilePage
from django.apps import apps


def profile_detail(request, profilepage_id):
    template = loader.get_template('profilepage.html')
    profile = ProfilePage.objects.get(id=profilepage_id)
    own_profile = False
    posts = []
    if profile.content_type.model == 'useraccount':
        Post = apps.get_model('post', 'Post')
        posts = Post.objects.filter(author=profile.subject.user)
        own_profile = request.user and (request.user.id == profile.subject.user.id)
    return HttpResponse(template.render({'profile': profile, 'posts': posts, 'own_profile': own_profile}, request))


