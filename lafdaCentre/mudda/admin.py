from django.contrib import admin
from .models import Mudda, SearchQuery, Comment, Profile, create_or_update_user_profile
# Register your models here.


# Register your models here.
admin.site.register(Mudda)
admin.site.register(SearchQuery)
admin.site.register(Profile)
admin.site.register(Comment)