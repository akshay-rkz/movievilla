from django.urls import path
from user import views

urlpatterns=[
    path('',views.userhome,name='userhome'),
    path('usergenre/<int:filmid>',views.usergenre,name='usergenre'),
    path('usersingleview/<int:movieid>',views.usersingleview,name='usersingleview'),
    path('viewusermovies',views.viewusermovies,name='viewusermovies'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('contact',views.contact,name='contact'),
    path('wishlist/<int:movieid>',views.wishlist,name='wishlist'),
    path('viewwish',views.viewwish,name='viewwish'),
    path('delete2/<int:deleteid>',views.delete2,name='delete2'),
    path('logout',views.logout,name='logout'),
    path('writecomments/<int:movieid>',views.writecomments,name='writecomments'),
    path('search',views.search,name='search'),
    path('like/<int:movieid>',views.like,name='like'),
    path('dislike/<int:movieid>',views.dislike,name='dislike'),
       
]