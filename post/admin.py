from django.contrib import admin
from .models import TweetStatus, LikeDislikeTweet, Tweet, Comment, LikeDislikeComment

admin.site.register(TweetStatus)
admin.site.register(LikeDislikeTweet)
admin.site.register(LikeDislikeComment)

admin.site.register(Tweet)
admin.site.register(Comment)


# Register your models here.
