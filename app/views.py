from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class Home(View):
    def get(self,request):
        return render(request,'app/home.html')

class School_list(ListView):
    model=School
    context_object_name='schools'
    #ordering=['name']

class School_detail(DetailView):
    model=School
    context_object_name='school'

class School_create(CreateView):
    model=School
    fields='__all__'


class School_update(UpdateView):
    model=School
    fields='__all__'


class School_delete(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('School_list')






    
