from django.contrib import admin
from posts.models import BlogPost




#@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "created_on",
        "last_updated",
    )

    list_editable = ("published",)
    search_fields = ("title", "content",)
    list_filter =("published", "last_updated")
    autocomplete_fields = ("author",)


admin.site.register(BlogPost, BlogPostAdmin) #we link our model BlogPost to our class BlogPostAdmin