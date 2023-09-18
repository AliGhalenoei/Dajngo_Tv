from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
import random
# import Apps...
from accounts.models import *
from content.models import *
from .serializers import *

# Create your views App Accounts...

class SingupAPIView(APIView):
    serializers_class = SingupSerializer

    def post(self,request):
        srz_data = self.serializers_class(data=request.POST)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            #srz_data.create(vd)
            User.objects.cretae_user(
                phone = vd['phone'],
                email = vd['email'],
                password = vd['password'],
            )
            return Response(data = srz_data.data)
        return Response(srz_data.errors)

# Create your views App Content...

# CRUD Category Api...
class ListCategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self,request):
        queryset = Category.objects.all()
        srz_data = self.serializer_class(instance=queryset,many=True)
        return Response(data=srz_data.data)
    
class RetrieveCategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self,request,slug):
        queryset = Category.objects.get(slug = slug)
        #lookup_field= ('slug',)
        srz_data = self.serializer_class(instance=queryset)
        return Response(data=srz_data.data)
    
class UpdateCategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self,request,slug):
        queryset = Category.objects.get(slug = slug)
        srz_data = self.serializer_class(instance=queryset)
        return Response(data=srz_data.data)
    
    def post(self,request,slug):
        queryset = Category.objects.get(slug = slug)
        srz_data = self.serializer_class(instance=queryset,data=request.POST,partial=True)
        if srz_data.is_valid():
            vd =srz_data.validated_data
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)
    
class DeleteCategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self,request,slug):
        queryset = Category.objects.get(slug = slug)
        queryset.delete()
        queryset.save()
        return Response({'massage':'Category Deleted...'})
    
# CRUD Movie Api...
class ListCreateMovieAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field='slug'

# CRUD Seryals...
class CRUD_SeryalMovieAPIView(viewsets.ViewSet):
    queryset=SeryalMovie.objects.all()
    serializer_class=SeryalMovieSerializer

    def list(self, request):
        srz_data = SeryalMovieSerializer(instance=self.queryset , many=True)
        return Response(data=srz_data.data)

    def create(self, request):
        srz_data = self.serializer_class(data=request.POST)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.get(id =pk)
        srz_data = self.serializer_class(instance=queryset , partial = True)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        queryset = self.queryset.get(id =pk)
        srz_data = self.serializer_class(instance=queryset,data=request.POST,partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)

    def destroy(self, request, pk=None):
        queryset = self.queryset.get(id =pk)
        queryset.delete()
        queryset.save()
        return Response({'massage':'Seryal Removed...'})

# Like Seryal And Movies...
class ListCreateLikeMovieAPIView(ListCreateAPIView):
    queryset = LikeMovie.objects.all()
    serializer_class = LikeMovieSerializer

class ListCreateLikeSeryalMovieAPIView(ListCreateAPIView):
    queryset = LikeSeryal.objects.all()
    serializer_class = LikeSeryalMovieSerializer

# Comments Seryal And Movies...
class CommentMovieAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentMovieSerializer

class RetrieveUpdateDestroyCommentMovieAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentMovieSerializer

class CommentSeryalMovieAPIView(ListCreateAPIView):
    queryset = CommentSeryal.objects.all()
    serializer_class = CommentSeryalMovieSerializer

class RetrieveUpdateDestroyCommentSeryalMovieAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentSeryal.objects.all()
    serializer_class = CommentSeryalMovieSerializer
    
            

class HomeAPIView(APIView):
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
class ListTrendMoviesAPIView(APIView):
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
class ListActionMoviesAPIView(APIView):
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
class ListExcitingMoviesAPIView(APIView):
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
class ListDramMoviesAPIView(APIView):
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
class ListLoveMoviesAPIView(APIView):
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
class ListScaryMoviesAPIView(APIView):
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

# List Seryals...
class ListSeryalsAPIView(APIView):
    template_name = 'content/list_seryals.html'

    def get(self,request):
        movies = SeryalMovie.objects.order_by('-id')
        paginator =Paginator(movies,2)
        paginator_page=(request.GET.get('page'))
        movies_list = paginator.get_page(paginator_page)
        return render(request,self.template_name,{
            'movies':movies_list,
        })

# List Category Page...    
class CategoryPageAPIView(APIView):
    template_name='content/list_category.html'

    def get(self,request):
        categorys = Category.objects.all()
        return render(request,self.template_name,{
            'categorys':categorys,
        })

# Filter Category Page...
class FilterCategoryPageAPIView(APIView):
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
    
# Details Movies...   
class DetailMoviesAPIView(APIView):
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
