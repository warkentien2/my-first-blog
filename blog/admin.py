from django.contrib import admin
from .models import Post

admin.site.register(Post)       # allows Post to be visible in admin's page
# Register your models here.
