from django.shortcuts import render ,redirect, get_object_or_404
from . models import Movieinfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def create(request):
    if request.POST:
         frm=MovieForm(request.POST, request.FILES)
         if frm.is_valid():
              frm.save()
              return redirect('list')
    else:
          frm=MovieForm()
    return render(request, 'create.html',{'frm':frm})

@login_required(login_url='login')
def list(request):
     recent_visits=request.session.get('recent_visits',[])
     count=request.session.get('count',0)
     count=count+1
     request.session['count']=count
     recent_movie_set=Movieinfo.objects.filter(pk__in=recent_visits)
     movie_set=Movieinfo.objects.all()
     print(movie_set)
     response=render(request, 'list.html', {
          'recent_movies':recent_movie_set,
          'movies':movie_set, 'visits':count})
     # response.set_cookie('visits',visits)
     return response


@login_required(login_url='login')
def edit(request,pk):
     
     instance_to_be_edited=Movieinfo.objects.get(pk=pk)
     if request.POST:

          # normal way
          frm = MovieForm(request.POST, request.FILES, instance = instance_to_be_edited)
          
          if frm.is_valid():
               frm.save()
               return redirect('list')
     else:
          recent_visits=request.session.get('recent_visits',[])
          recent_visits.insert(0,pk)
          request.session['recent_visits']=recent_visits
          
          frm=MovieForm(instance=instance_to_be_edited)
     return render(request,'create.html',{'frm':frm})


@login_required(login_url='login')
def delete(request,pk):
     try:
          instance=Movieinfo.objects.get(pk=pk)
          instance.delete()
     except Movieinfo.DoesNotExist:
          return redirect('list')
     
     movie_set=Movieinfo.objects.all()
     return render(request, 'list.html', { 'movies':movie_set} )
