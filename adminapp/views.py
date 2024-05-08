from django.shortcuts import render,redirect
from adminapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from user.models import *

# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')

def admincategories(request):
    if request.method=='POST':
        categories=request.POST['categories']
        image=request.FILES['image']

        Genres.objects.create(
            genre_name=categories,
            images=image
        )
    return render(request,'admincategories.html')

def viewcategories(request):
    details=Genres.objects.all()
    context={'details':details}
    return render(request,'viewcategories.html',context)

def delete(request,nameid):
    Genres.objects.filter(id=nameid).delete()
    return redirect('viewcategories')

def addmovies(request):
    genres = Genres.objects.all()
    context = {
        'genres':genres,
    }
    if request.method == "POST":
        movie_genre = request.POST['genres']
        movie_name = request.POST['movie_name']
        director_name = request.POST['director_name']
        duration = request.POST['duration']
        poster = request.FILES['poster']
        movie = request.FILES['movie']

        Movies.objects.create(
            genre_id = Genres.objects.get(id=movie_genre),
            movie_name = movie_name,
            director = director_name,
            movie_duration = duration,
            movie_poster = poster,
            movie_file = movie
        )
    return render(request,'addmovies.html', context)

def viewmovies(request):
    movie=Movies.objects.all()
    context={
        'movie':movie,
    }
    return render(request,'viewmovie.html',context)

def edit(request,editid):
    data=Movies.objects.filter(id=editid)
    selected_genre = Movies.objects.get(id=editid).genre_id
    
    genre_details = Genres.objects.all()
    context={
        'data':data,
        'genre_details':genre_details,
        'selected_genre':selected_genre,
    }
    return render(request,'edit.html',context)

def update(request,updateid):
    if request.method=='POST':
        movie_genre = request.POST['genres']
        movie_name = request.POST['movie_name']
        director_name = request.POST['director_name']
        duration = request.POST['duration']
        try:
            image=request.FILES['poster']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=Movies.objects.get(id=updateid).movie_poster
        Movies.objects.filter(id=updateid).update(
            genre_id= movie_genre,
            movie_name=movie_name,
            director=director_name,
            movie_duration=duration,
            movie_poster=file
        )
        return redirect('viewmovies')          
    return render(request,'edit.html')
    
def delete_movies(request,nameid):
    Movies.objects.filter(id=nameid).delete()
    return redirect('viewmovies')


def add_movie_cast(request):
    cast=Movies.objects.all()
    context={
        'cast':cast
    }
    return render(request, "add_movie_cast.html",context)

def addcast(request, movieid):
    if request.method=='POST':
        castname=request.POST['castname']
        castimage=request.FILES['castimage']

        Cast.objects.create(
            movie_id=Movies.objects.get(id=movieid),
            castname=castname,
            castimage=castimage
        )
    context = {
        'movieid':movieid,
    }
    return render(request,'addcast.html', context)

def viewcast(request, movieid):
    moviecast=Cast.objects.filter(movie_id=movieid)
    context={
        'moviecast':moviecast
    }
    return render(request,'viewcast.html',context)

def deletecast(request,castid):
    Cast.objects.filter(id=castid).delete()
    return redirect('viewcast')

def addnotification(request):
    if request.method=='POST':
        heading=request.POST['heading']
        message=request.POST['message']

        Notification.objects.create(
            heading=heading,
            message=message
        )
    return render(request,'addnotification.html')

def viewnotification(request):
    noti=Notification.objects.all()
    context={
        'noti':noti
    }
    return render(request,'viewnotification.html',context)

def deletenotification(request,messageid):
    Notification.objects.filter(id=messageid).delete()
    return redirect('viewnotification')

def viewcomplaints(request):
    complaints=Contact.objects.all()
    context={
        'complaints':complaints
    }
    return render(request,'viewcomplaints.html',context)

def viewusers(request):
    users=Customer.objects.all()
    context={
        'users':users
    }
    return render(request,'viewusers.html',context)

def deleteusers(request,nameid):
    Customer.objects.filter(id=nameid).delete()
    return redirect('viewusers')

def adminlogout(request):
    return redirect('userhome')

