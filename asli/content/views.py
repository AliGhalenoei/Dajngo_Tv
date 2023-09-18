from typing import Any
from django import http
from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.mail import send_mail
import random
from .models import *
from .forms import *
# Create your views here.

class HomeView(View):
    template_name='content/home.html'

    def get(self,request):
        categorys = Category.objects.all()
        # Slider Header Site...
        slider=Movie.objects.all()
        random_slider = random.sample(list(slider),k=3)
        # Trends Movies...
        trends = Movie.objects.order_by('-id')[:4] 
        # Filter Action Movies...
        category_action = Category.objects.get(name='اکشن')
        action_movies = Movie.objects.filter(category=category_action)[:4]
        # Filter Exciting Movies...
        category_dram = Category.objects.get(name='هیجان انگیز')
        exciting_movies = Movie.objects.filter(category=category_dram)[:4]
        # Filter Dram Movies...
        category_dram = Category.objects.get(name='درام')
        dram_movies = Movie.objects.filter(category=category_dram)[:4]
        # Filter Loves Movies...
        category_love = Category.objects.get(name='عاشقانه')
        love_movies = Movie.objects.filter(category=category_love)[:4]
        # Filter Scary Movies...
        category_scary = Category.objects.get(name='ترسناک')
        scary_movies = Movie.objects.filter(category=category_scary)[:4]
        # Filter Seyals...
        seryal_movies = SeryalMovie.objects.order_by('-id')


        return render(request,self.template_name,{
            'categorys':categorys,
            'slider':random_slider,            
            # filter Movies Query...
            'trends':trends,
            'action_movies':action_movies,
            'exciting_movies':exciting_movies,
            'dram_movies':dram_movies,
            'love_movies':love_movies,
            'scary_movies':scary_movies,
            # Seryals...
            'seryal_movies':seryal_movies, 

        })
# List Trend Movies...
class ListTrendMoviesView(View):
    template_name='content/list_trend_movies.html'

    def get(self,request):
        movies = Movie.objects.order_by('-id')
        paginator = Paginator(movies,8)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    
# List Action Movies...   
class ListActionMoviesView(View):
    template_name='content/list_action_movies.html'

    def get(self,request):
        category_action = Category.objects.get(name='اکشن')
        movies = Movie.objects.filter(category=category_action)
        paginator = Paginator(movies,4)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    
# List Exciting Movies...   
class ListExcitingMoviesView(View):
    template_name='content/list_exciting_movies.html'

    def get(self,request):
        category_exciting = Category.objects.get(name='هیجان انگیز')
        movies = Movie.objects.filter(category=category_exciting)
        paginator = Paginator(movies,4)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    
# List Dram Movies...   
class ListDramMoviesView(View):
    template_name='content/list_dram_movies.html'

    def get(self,request):
        category_dram = Category.objects.get(name='درام')
        movies = Movie.objects.filter(category=category_dram)
        paginator = Paginator(movies,4)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    
# List Love Movies...   
class ListLoveMoviesView(View):
    template_name='content/list_love_movies.html'

    def get(self,request):
        category_love = Category.objects.get(name='عاشقانه')
        movies = Movie.objects.filter(category=category_love)
        paginator = Paginator(movies,4)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    
# List Scary Movies...   
class ListScaryMoviesView(View):
    template_name='content/list_scary_movies.html'

    def get(self,request):
        category_scary = Category.objects.get(name='ترسناک')
        movies = Movie.objects.filter(category=category_scary)
        paginator = Paginator(movies,4)
        paginator_page = request.GET.get('page')
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })
    

# Code Serach Navbar 
class SearchMoviesView(View):
    template_name='content/search.html'

    def get(self,request):
        movies = Movie.objects.all()
        seryals = SeryalMovie.objects.all()
        if request.GET.get('search'):
            movies = movies.filter(name__contains=request.GET['search'])
        if request.GET.get('search'):
            seryals = seryals.filter(name__contains=request.GET['search'])
        return render(request,self.template_name,{
            'movies':movies,
            'seryals':seryals,
        })

# Details Movies...   
class DetailMoviesView(View):
    template_name='content/detail.html'

    def get(self,request,slug):
        movies = Movie.objects.all()
        movie = Movie.objects.get(slug=slug)
        # get all Comment movies
        comments = Comment.objects.filter(movie = movie)
        # Random Movies...
        random_movies = random.sample(list(movies),k=4)
        return render(request,self.template_name,{
            'movie':movie,
            'random_movies':random_movies,
            'comments':comments
        })
    
    def post(self,request,slug):
        comment = request.POST.get('comment')
        movie = Movie.objects.get(slug=slug)
        Comment.objects.create(
            user = request.user,
            movie=movie,
            comment = comment,
        )
        return redirect('home')
    
class PlayMoviePageView(View):
    template_name='content/play_movie.html'

    def get(self,request,slug):
        movie = Movie.objects.get(slug=slug)
        return render(request,self.template_name,{
            'movie':movie
        })
    
# Update And Delete Comment Views...

class UpdateCommentView(View):
    from_class = UpdateCommentForm
    template_name = 'content/update_comment.html'

    def setup(self, request, *args: Any, **kwargs: Any) -> None:
        self.movie_ins = Comment.objects.get(id = kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args: Any, **kwargs: Any):
        movie = self.movie_ins
        if not movie.user == request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,pk):
        movie = self.movie_ins
        form = self.from_class(instance=movie)
        return render(request,self.template_name,{
            'form':form
        })
    
    def post(self,request,pk):
        commnt_ins = Comment.objects.get(id=pk)
        form = self.from_class(request.POST , instance=commnt_ins)
        if form.is_valid():
            print('=====>>>' * 5)
            form.save()
            return redirect('home')
        return render(request,self.template_name,{'form',form})
    
class DeleteCommentView(View):

    def get(self,request,pk):
        comment_user = Comment.objects.get(id=pk)
        if comment_user.user == request.user:
            comment_user.delete()
            return redirect('home')
        else:
            return redirect('home')
        
# Save And Like Movie Views...

class SaveMovieView(View):

    def get(self,request,slug):
        movie = Movie.objects.get(slug = slug)
        test=SaveMovie.objects.filter(user = request.user ,movie = movie).exists()
        if test:
            return redirect('home')
        else:
            SaveMovie.objects.create(user = request.user ,movie = movie)
            return redirect('home')
        
class UnSaveMovieView(View):

    def get(self,request,slug):
        movie = Movie.objects.get(slug = slug)
        test=SaveMovie.objects.filter(user = request.user ,movie = movie)
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')
    
class ListSaveMoviesView(View):
    template_name = 'content/list_save_movies.html'

    def get(self,request,pk):
        movies = SaveMovie.objects.filter(user = pk)
        seryals = SaveSeryal.objects.filter(user = pk)

        return render(request,self.template_name,{
            'movies':movies,
            'seryals':seryals
        })
    
class LikeMovieView(View):

    def get(self,request,slug):
        movie = Movie.objects.get(slug = slug)
        test = LikeMovie.objects.filter(user = request.user , movie = movie).exists()
        if test:
            return redirect('home')
        else:
            LikeMovie.objects.create(user = request.user , movie = movie)
            return redirect('home')
        
class DisLikeMovieView(View):

    def get(self,request,slug):
        movie = Movie.objects.get(slug = slug)
        test = LikeMovie.objects.filter(user = request.user , movie = movie)
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')
        
# Page Category...

class CategoryPageView(View):
    template_name='content/list_category.html'

    def get(self,request):
        categorys = Category.objects.all()
        return render(request,self.template_name,{
            'categorys':categorys,
        })

class FilterCategoryPageView(View):
    template_name = 'content/filter_category.html'

    def get(self,request,slug):
        category = Category.objects.get(slug=slug)
        movies = Movie.objects.filter(category = category)
        paginator =Paginator(movies,4)
        paginator_get = request.GET.get('page')
        movies_list = paginator.get_page(paginator_get)
        return render(request,self.template_name,{
            'movies':movies_list,
        })

# Contact Page...

class ContactView(View):
    template_name = 'content/contact.html'

    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        msg = 'name:{0} , email:{1} , phone:{2} , subject:{3} , body:{4}'.format(name,email,phone,subject,body)
        send_mail(subject,msg,'alighalenoei8383@gmail.com',['alighalenoei8383@gmail.com'],fail_silently=False)
        return redirect('home')
    
# Detail Seryals...
class DetailSeryalView(View):
    template_name ='content/detail_seryals.html'

    def get(self,request,pk):
        movies = Movie.objects.all()
        movie = SeryalMovie.objects.get(id = pk)
        videos=UploadPartSeryal.objects.filter(seyal=pk)
        random_movies = random.sample(list(movies),k=4)
        comments = CommentSeryal.objects.filter(movie = movie)
        return render(request,self.template_name,{
            'movie':movie,
            'random_movies':random_movies,
            'comments':comments,
            'videos':videos,
        })
    
    def post(self,request,pk):
        comment = request.POST.get('comment')
        o = SeryalMovie.objects.get(id = pk)
        CommentSeryal.objects.create(
            user = request.user,
            movie = o,
            comment = comment,            
        )
        return redirect('home')
    
# Update and Delete Comment Seryal...

class UpdateCommentSeryalView(View):
    from_class = UpdateCommentSeryalForm
    template_name = 'content/update_commentseryal.html'

    def setup(self, request, *args: Any, **kwargs: Any) -> None:
        self.movie_ins = CommentSeryal.objects.get(id = kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args: Any, **kwargs: Any):
        movie = self.movie_ins
        if not movie.user == request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,pk):
        movie = self.movie_ins
        form = self.from_class(instance=movie)
        return render(request,self.template_name,{
            'form':form
        })
    
    def post(self,request,pk):
        commnt_ins = CommentSeryal.objects.get(id=pk)
        form = self.from_class(request.POST , instance=commnt_ins)
        if form.is_valid():
            print('=====>>>' * 5)
            form.save()
            return redirect('home')
        return render(request,self.template_name,{'form',form})
    
class DeleteCommentSeryalView(View):

    def get(self,request,pk):
        comment_user = CommentSeryal.objects.get(id=pk)
        if comment_user.user == request.user:
            comment_user.delete()
            return redirect('home')
        else:
            return redirect('home')
        
# List Seryals (Navbar)

class ListSeryalsView(View):
    template_name = 'content/list_seryals.html'

    def get(self,request):
        movies = SeryalMovie.objects.order_by('-id')
        paginator =Paginator(movies,2)
        paginator_page=(request.GET.get('page'))
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })

  # Play Seryal  
class PlaySeryal(View):
    template_name='content/play_seryal.html'

    def get(self,request,pk):
        movie = UploadPartSeryal.objects.get(id=pk)
        return render(request,self.template_name,{
            'movie':movie
        })
    
# Save And Like Seryal...

class SaveSeryalView(View):

    def get(self,request,slug):
        seryal = SeryalMovie.objects.get(slug = slug)
        test = SaveSeryal.objects.filter(
            user = request.user,
            movie = seryal
        ).exists()
        if test:
            return redirect('home')
        else:
            SaveSeryal.objects.create(
                user = request.user,
                movie = seryal
            )
            return redirect('home')

class UnSaveSeryalView(View):

    def get(self,request,slug):
        movie = SeryalMovie.objects.get(slug = slug)
        test = SaveSeryal.objects.filter(user = request.user , movie = movie)
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')
        
class LikeSeryalView(View):

    def get(self,request,slug):
        movie = SeryalMovie.objects.get(slug = slug)
        test = LikeSeryal.objects.filter(user = request.user , movie = movie).exists()
        if test:
            return redirect('home')
        else:
            LikeSeryal.objects.create(user = request.user , movie = movie)
            return redirect('home')
        
class DisLikeSeryalView(View):

    def get(self,request,slug):
        movie = SeryalMovie.objects.get(slug = slug)
        test = LikeSeryal.objects.filter(user = request.user , movie = movie)
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')

        

    

    
        


    


        


    

