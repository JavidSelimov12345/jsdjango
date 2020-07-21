from django.contrib.admin import ModelAdmin, register
from .models import Post
# Register your models here.


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'content', 'author')
    icon_name = 'message'


