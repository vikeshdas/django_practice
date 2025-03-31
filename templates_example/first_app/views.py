from django.shortcuts import render
from .models import Topic

def topic_list(request):
    topics = Topic.objects.all()  
    return render(request, 'first_app/index.html', {'topics': topics})
