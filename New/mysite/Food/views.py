from django.shortcuts import render ,redirect
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import loader

# Create your views here.
## index is the name of the python function
def index(request):
    item_list=Item.objects.all()
    template= loader.get_template('Food/index.html')
    context={
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))

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
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Food:index')
    
    return render(request,'Food/item-form.html',{'form':form})
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

