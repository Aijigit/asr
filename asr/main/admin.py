from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
  list_display = ("title", "date_added",)
  prepopulated_fields = {"slug": ("title", "category")}
 
class AwardsAdmin(admin.ModelAdmin):
  list_display = ("title",)
  search_fields = ('description', )
  prepopulated_fields = {"slug": ("title", )}


class NewsAdmin(admin.ModelAdmin):
  list_display = ("title", "category")
  search_fields = ('title', "short_description")
  prepopulated_fields = {"slug": ("title", )}
  
   
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Awards, AwardsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory)
admin.site.register(NewsImage)
admin.site.register(Partners)
admin.site.register(Team)
admin.site.register(ProjectImage)
