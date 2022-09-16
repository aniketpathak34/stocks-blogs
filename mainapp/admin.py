from django.contrib import admin
from .models import StockDetail, Profile, Comment
# Register your models here.
admin.site.register(StockDetail)
admin.site.register(Profile)


from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)