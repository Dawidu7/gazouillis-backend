from django.db import models

# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    parent_tweet = models.ForeignKey('Tweet', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    likes = models.ManyToManyField('users.User', related_name='likes', blank=True)

    def __str__(self):
        return self.body[:20] if len(self.body) > 20 else self.body