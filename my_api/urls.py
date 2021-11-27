from django.urls import path
from .views import PostList, PostDetail ,Createuser


urlpatterns = [

    path('blogs/', PostList.as_view(), name='listcreate'),
    path('blogs/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('user/', Createuser.as_view()),
    

    
]