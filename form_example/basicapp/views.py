from django.shortcuts import render
from basicapp import forms

def index(request):
    return render(request,'basicform/index.html')

def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request,'basicform/form_page.html',{'form':form})


