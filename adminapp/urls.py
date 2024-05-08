from django.urls import path
from adminapp import views

urlpatterns=[
    path('adminhome',views.adminhome,name='adminhome'),
    path('admincategories',views.admincategories,name='admincategories'),
    path('viewcategories',views.viewcategories,name='viewcategories'),
    path('delete<int:nameid>',views.delete,name='delete'),
    path('addmovies',views.addmovies,name='addmovies'),
    path('viewmovies',views.viewmovies,name='viewmovies'),
    path('edit/<int:editid>',views.edit,name='edit'),
    path('update/<int:updateid>',views.update,name='update'),
    path('delete_movies/<int:nameid>',views.delete_movies,name='delete_movies'),
    path('add_movie_cast',views.add_movie_cast,name='add_movie_cast'),
    path('addcast/<int:movieid>',views.addcast,name='addcast'),
    path('viewcast/<int:movieid>',views.viewcast,name='viewcast'),
    path('deletecast/<int:castid>',views.deletecast,name='deletecast'),
    path('addnotification',views.addnotification,name='addnotification'),
    path('viewnotification',views.viewnotification,name='viewnotification'),
    path('deletenotification/<int:messageid>',views.deletenotification,name='deletenotification'),
    path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('deleteusers/<int:nameid>',views.deleteusers,name='deleteusers'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    
]
