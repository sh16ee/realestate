from django.contrib import admin
from .models import Post, UserProfile, Agency, Comment

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Agency)
admin.site.register(Comment)
