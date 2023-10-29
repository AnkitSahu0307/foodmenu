from . import views
from django.urls import path , include


app_name='Food'
urlpatterns = [
    ## /food/
    path('',views.IndexClassView.as_view(),name='index'),    
    path('item/',views.view,name='item'),
    path('item/feedback',views.feed,name='feedback'), ## item/feedback pe aaega ye 
    ##/feedback --- se food/feedback ke baad aaega view
   ## food/1/
   path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
   #add item for forms
    path('add',views.CreateItem.as_view(),name='create_item'),
 #edit/ update item
 path('update/<int:id>/',views.update_item,name='update_item'),
 #delete an item
 path('delete/<int:id>/',views.delete_item,name='delete_item'),
]