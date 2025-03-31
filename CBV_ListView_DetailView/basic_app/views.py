from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)
from basic_app import models
from django.urls import reverse_lazy



class SchoolListView(ListView):
    context_object_name = 'schools' 

    model = models.School

class SchoolDetailview(DetailView):

    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolCreateView(CreateView):
    fields = ('name','principal', 'location')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class IndexView(TemplateView):

    template_name = 'index.html' 
