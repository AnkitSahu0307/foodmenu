from django.forms.models import BaseModelForm
from django.shortcuts import render ,redirect
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
## index is the name of the python function
def index(request):
    item_list=Item.objects.all()
    template= loader.get_template('Food/index.html')

    context={
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))

class IndexClassView(ListView):
    model=Item;
    template_name='Food/index.html';
    context_object_name='item_list';

def view(request):
    return HttpResponse('this is an item view')
def feed(request):
    return HttpResponse('<h1> tis is an feedback page</h1>')
def detail(request , item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request , 'Food/detail.html' , context)
   # return HttpResponse("this is item no/id : %s" % item_id)

class FoodDetail(DetailView):
    model=Item;
    template_name='Food/detail.html'
    
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Food:index')
    
    return render(request,'Food/item-form.html',{'form':form})

#this is class based view for create_item

class CreateItem(CreateView):
    model=Item;
    fields=['item_name','item_desc','item_price','item_image']
    template_name='Food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user
        
        return super().form_valid(form)
    
    
def update_item(request,id):
    item= Item.objects.get(id=id)
    form = ItemForm(request.POST or None , instance=item)

    if form.is_valid():
        form.save()
        return redirect('Food:index')
    return render(request,'Food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item= Item.objects.get(id=id) #hame item ka id chahiye 
    
    if request.method =='POST':
        item.delete()
        return redirect('Food:index')
    return render(request,'Food/item-delete.html',{'item':item})

