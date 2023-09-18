from django.db import models
from accounts.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Category_Movie_Info(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        abstract=True

# class Tag_Movis(models.Model):
#     name=models.CharField(max_length=255)

class Category(Category_Movie_Info):
    img = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
class Movie(Category_Movie_Info):
    category=models.ManyToManyField(Category,related_name='cate_movie')
    img=models.ImageField(upload_to="images/")
    time=models.CharField(max_length=255)
    worning=models.CharField(max_length=3)
    date=models.CharField(max_length=20)
    movie=models.FileField(upload_to="movies/")
    abut=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie_comment')
    comment=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} Commented... {self.movie}'
    
class SaveMovie(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_save',null=True,blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='save_movie')

    def __str__(self) -> str:
        return str(self.movie)
    
class LikeMovie(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_like')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='like_movie')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} Liked Movie... {self.movie}'

# Seryal Movies...
    
class SeryalMovie(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=200,unique=True)
    category=models.ManyToManyField(Category,related_name='part_movie')
    #part = models.ManyToManyField(SelectPartSeryal,related_name='part_seryal')
    img=models.ImageField(upload_to="images/")
    time=models.CharField(max_length=255)
    worning=models.CharField(max_length=3)
    date=models.CharField(max_length=20)
    abut=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
class UploadPartSeryal(models.Model):
    seyal = models.ForeignKey(SeryalMovie,on_delete=models.CASCADE,related_name='upload_part')
    num_part = models.CharField(max_length=50)
    part = models.FileField(upload_to='movies/')

    def __str__(self) -> str:
        return self.num_part

class CommentSeryal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment_seryal')
    movie=models.ForeignKey(SeryalMovie,on_delete=models.CASCADE,related_name='seryal_comment')
    comment=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} Commented... {self.movie}'

class SaveSeryal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_save_seryal',null=True,blank=True)
    movie = models.ForeignKey(SeryalMovie,on_delete=models.CASCADE,related_name='save_seryal')

    def __str__(self) -> str:
        return str(self.movie)

class LikeSeryal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_like_seryal')
    movie = models.ForeignKey(SeryalMovie,on_delete=models.CASCADE,related_name='like_seryal')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} Liked Movie... {self.movie}'




    



    
    

    
