from .import views
from django.urls import path, include

urlpatterns = [

    path('',views.add,name='home.html'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvlhome/',views.Tasklist.as_view(),name='cvlhome'),
    path('cvldetail/<int:pk>/',views.Taskdetail.as_view(),name='cvldetail'),
    path('cvlupdate/<int:pk>/',views.Taskupdate.as_view(),name='cvlupdate'),
    path('cvldelete/<int:pk>/', views.Taskdelete.as_view(), name='cvldelete')
]
