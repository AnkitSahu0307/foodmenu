from . import views
from django.urls import path , include


app_name='Food'
urlpatterns = [
    ## /food/
    path('',views.index,name='index'),    
    path('item/',views.view,name='item'),
    path('item/feedback',views.feed,name='feedback'), ## item/feedback pe aaega ye 
    ##/feedback --- se food/feedback ke baad aaega view
   ## food/1/
   path('<int:item_id>/',views.detail,name='detail'),
   #add item for forms
    path('add',views.create_item,name='create_item'),
 #edit/ update item
 path('update/<int:id>/',views.update_item,name='update_item'),
 #delete an item
 path('delete/<int:id>/',views.delete_item,name='delete_item'),
]