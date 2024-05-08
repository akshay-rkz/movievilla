from django.shortcuts import render, redirect
from adminapp.models import *
from user.models import *
from django.db.models import Subquery
from django.http import HttpResponse



# Create your views here.
def userhome(request,):
    username = request.session.get('username')
    homes=Genres.objects.all()
    movies=Movies.objects.all()[:6]
    films=Movies.objects.all()[:3]
    notification=Notification.objects.all()
    
    context={
        'homes':homes,
        'username':username,
        'movies':movies,
        'films':films,
        'notification':notification
    }
    return render(request,'userhome.html',context)

def usergenre(request,filmid):
    homes=Genres.objects.all()
    genr=Movies.objects.filter(genre_id=filmid)
    context={
        'homes':homes,
        'genr':genr,
    }
    return render(request,'usergenre.html',context)

def usersingleview(request,movieid):
    if 'u_id' in  request.session:
        films=Movies.objects.filter(id=movieid)
        castename=Cast.objects.filter(movie_id=movieid)
        comment=Comments.objects.filter(movieid=movieid)
        homes=Genres.objects.all()
        likecount=Likes.objects.filter(movieid=movieid).count()
        dislikecount=DISlikes.objects.filter(movieid=movieid).count()
        context={
            'films':films,
            'castename':castename,
            'comment':comment,
            'homes':homes,
            'likecount':likecount,
            'dislikecount':dislikecount,
        }
        return render(request,'usersingleview.html',context)
    else:
        return redirect('userlogin')

def viewusermovies(request):
    single=Movies.objects.all()
    homes=Genres.objects.all()
    context={
        'single':single,
        'homes':homes
    }
    return render(request,'viewusermovies.html',context)

def userlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']


        if email == "admin123@gmail.com" and password == "admin123":
            return redirect('adminhome')

        elif Customer.objects.filter(email = email, password=password).exists():
            data = Customer.objects.filter(email = email, password=password).values('username', 'id','email').first()
            request.session['username'] = data['username']
            request.session['u_id'] = data['id']
            request.session['email']=data['email']
            
            return redirect('userhome')
        else:
            return redirect('userlogin')
    
    return render(request,'userlogin.html')

def usersignup(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        confirmpass=request.POST['confirmpassword']
        if password==confirmpass:
         Customer.objects.create(
            email=email,
            username=username,
            password=password,
            phonenumber=phonenumber,
        )
        else:
            return redirect('usersignup') 
    return render(request,'usersignup.html')

def contact(request):
    userid=request.session.get('u_id')
    user_email = Customer.objects.get(id=userid).email
    homes=Genres.objects.all()
    context={
        'homes':homes,
        'user_email':user_email
    }
    if request.method=='POST':
        message=request.POST['message']

        Contact.objects.create(
            message=message,
            userid=Customer.objects.get(id=userid)
        )
    return render(request,'contact.html',context)

def wishlist(request,movieid):
    user=request.session.get('u_id')

    Wishlist.objects.create(
       userid=Customer.objects.get(id=user),
       films=Movies.objects.get(id=movieid) 
    )
    
    return redirect('viewusermovies')

def viewwish(request):
    user_id=request.session.get('u_id')
    view=Wishlist.objects.filter(userid=user_id)
    homes=Genres.objects.all()
    context={
        'view':view,
        'homes':homes,
    }
    return render(request,'wishlist.html',context)

def delete2(request,deleteid):
    Wishlist.objects.filter(id=deleteid).delete()
    return redirect('viewwish')

def logout(request):
    del request.session['u_id']
    del request.session['username']
    del request.session['email']
    return redirect('usersignup')

def writecomments(request,movieid):
    userid=request.session.get('u_id')
    
    if request.method=='POST':
        comment=request.POST['comment']
        
        Comments.objects.create(
            userid=Customer.objects.get(id=userid),
            movieid=Movies.objects.get(id=movieid),
            comment=comment
        )
        return redirect(f'/usersingleview/{movieid}')
    return render(request,'usersingleview.html')

def search(request):
    search_name=request.GET['search'] 
    if search_name:
        movies_by_name = Movies.objects.filter(movie_name__icontains=search_name)
        matching_genres = Genres.objects.filter(genre_name__icontains=search_name)
        movies_by_genre = Movies.objects.filter(genre_id__in=matching_genres)
        films = movies_by_name | movies_by_genre
        context={
        'films':films
        }
        return render(request,'search.html',context)
    else:
        return redirect('userhome')

def like(request,movieid):
    userid=request.session.get('u_id')
    if not Likes.objects.filter(userid=userid, movieid=movieid).exists():
        Likes.objects.create(
            userid=Customer.objects.get(id=userid),
            movieid=Movies.objects.get(id=movieid),
        )   
        DISlikes.objects.filter(
            userid=Customer.objects.get(id=userid),
            movieid=Movies.objects.get(id=movieid),
        ).delete()
        return redirect(f'/usersingleview/{movieid}')
    return render(request,'usersingleview.html')

def dislike(request,movieid):
    userid=request.session.get('u_id')
    if not DISlikes.objects.filter(userid=userid, movieid=movieid).exists():
        DISlikes.objects.create(
            userid=Customer.objects.get(id=userid),
            movieid=Movies.objects.get(id=movieid),
        )   
        Likes.objects.filter(
            userid=Customer.objects.get(id=userid),
            movieid=Movies.objects.get(id=movieid),
        ).delete()
        return redirect(f'/usersingleview/{movieid}')
    return render(request,'usersingleview.html')


