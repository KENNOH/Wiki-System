from django.contrib import admin
from .models import WikiSearch
# Register your models here.

class WikiSearchModelAdmin(admin.ModelAdmin):
    list_display = ['unique_id',"title",'views','is_published','description','created_at',]
    list_display_links = ["unique_id"]
    search_fields = ["title","unique_id"]
    readonly_fields = ('unique_id','views')
    

    class Meta:
        model = WikiSearch

    
admin.site.register(WikiSearch, WikiSearchModelAdmin)



admin.site.site_header = 'Wiki System Admin Panel'
admin.site.site_title = "Wiki System Admin Portal"
admin.site.index_title = "Welcome to the Wiki System Admin Portal"