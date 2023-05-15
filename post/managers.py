from django.db import models

class FeedManager(models.Manager):
    def get_feed(self, request):
        return self.exclude(author=request.user.id).order_by('-created_on')