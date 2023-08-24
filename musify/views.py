from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import songs,likedsongs
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Case,When


# Create your views here.
def home(request):
    song=songs.objects.all()
    trending_songs = songs.objects.filter(trending=True)
    arijit_songs=songs.objects.filter(singer="Arijit Singh")
    if request.user.is_authenticated:
        ls = likedsongs.objects.filter(user=request.user)
        id = []
        for i in ls:
            id.append(i.music_id)
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(id)])
        liked = songs.objects.filter(song_id__in=id).order_by(preserved) 
    
    else:
        liked= songs.objects.all()

    return render(request,'musify/index.html', {'songs': song, 'liked': liked,'trending_songs':trending_songs,'arijit_songs':arijit_songs})
    

def allsongs(request):
    song=songs.objects.all()
    return render(request,"musify/allsongs.html",{'songs':song})



def songpage(request,id):
    song=songs.objects.filter(song_id=id).first()
    return render(request,"musify/songpage.html",{'songs':song})

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        myuser=User.objects.create_user(username,email,password1)
        myuser.firstname=firstname
        myuser.lastname=lastname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        from django.contrib.auth import authenticate,login,logout
        user=authenticate(username=username,password=password1)
        login(request,user)
        return redirect('/')
    return render(request,"musify/signup.html")
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        from django.contrib.auth import authenticate,login,logout
        user = authenticate(username=username, password=password1)
        from django.contrib.auth import login
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request, "Wrong Credentials!!")
            return redirect('login')
        
        #login(request, user)   
        #return redirect("/")
    return render(request,"musify/login.html")

def logout(request):
    from django.contrib.auth import authenticate,login,logout
    logout(request)

    return redirect('home')

def likedsong(request):
    if request.method=="POST":
        user= request.user
        music_id=request.POST.get('music_id')

        liked=likedsongs.objects.filter(user=user)
        for i in liked:
            if music_id==i.music_id:
                message='Song is already added'
                break
        else:

            likedsong=likedsongs(user=user,music_id=music_id)
            likedsong.save()
            message="Song is succesffuly added"
        song=songs.objects.filter(song_id=music_id).first()
        return render(request,"musify/songpage.html",{'songs':song,"message":message})
    ls=likedsongs.objects.filter(user=request.user)
    id=[]
    for i in ls:
        id.append(i.music_id)
    preserved= Case(*[When(pk=pk,then=pos)for pos,pk in enumerate(id)])
    song=songs.objects.filter(song_id__in=id).order_by(preserved)

    return render(request,"musify/likedsongs.html",{'songs':song})

def trending_songs(request):
    trending_songs = songs.objects.filter(trending=True)
    return render(request,"musify/trending.html",{'trending_songs':trending_songs})

def arijit(request):
    arijit_songs=songs.objects.filter(singer="Arijit Singh")
    return render(request,"musify/arijit.html",{'arijit_songs':arijit_songs})

def search(request):
    query=request.GET.get("query")
    song=songs.objects.all()
    qs=song.filter(name__icontains=query)
    qm=song.filter(movie__icontains=query)
    qsi=song.filter(singer__icontains=query)
    smq=qs.union(qm).union(qsi)
    context = {"songs": smq, "query": query}
    if smq.exists():
        return render(request,'musify/search.html',{"songs":smq,"query":query})
    else:
        no_results_message = f"No results found for '{query}'."
        context["no_results_message"] = no_results_message
        return render(request, 'musify/search.html', context)


