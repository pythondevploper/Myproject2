from .forms import Todo
from django.shortcuts import render,redirect
from .  models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
class Tasklistview(ListView):
   model=Task
   template_name='home.html'
   context_object_name='task1'
class Taskdetailview(DetailView):
   model=Task
   template_name='details.html'
   context_object_name='task'
class Taskupdateview(UpdateView):
   model=Task
   template_name='update.html'
   context_object_name='task'
   fields=('name','priority','date')  

class Taskdeleteview(DeleteView):
   model=Task
   template_name='delete.html'
   success_url=reverse_lazy('cbvhome') 
   
   def get_success_url(self):
      return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})



def demo(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})   

def delete(request,taskid):
   task=Task.objects.get(id=taskid) 
   if request.method=='POST':
    task.delete()
    return redirect('/')
   return render(request,'delete.html')
def update(request,id):
   task=Task.objects.get(id=id)

def update(request,id):
   task=Task.objects.get(id=id)
   f=Todo(request.POST or None, instance=task) 
   if f.is_valid():
       f.save() 
       return redirect('/')
   return render(request,'edit.html',{'f':f,'task':task})
#def details(request):

 #   return render(request,'details.html')
# Create your views here.
