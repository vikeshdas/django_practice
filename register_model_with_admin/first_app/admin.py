from django.contrib import admin
from .models import Topic

# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic_name') 
admin.site.register(Topic)
 