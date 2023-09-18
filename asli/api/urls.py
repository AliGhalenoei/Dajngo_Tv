from django.urls import path
from rest_framework import routers
from .import views

urlpatterns = [
    # Accounts. app urls...
    path('singup_api/',views.SingupAPIView.as_view(),name='singup_api'),
    # CRUD Category...
    path('list_category_api/',views.ListCategoryAPIView.as_view(),name='list_category_api'),
    path('retrieve_category_api/<slug:slug>/',views.RetrieveCategoryAPIView.as_view(),name='retrieve_category_api'),
    path('update_category_api/<slug:slug>/',views.UpdateCategoryAPIView.as_view(),name='update_category_api'),
    path('delete_category_api/<slug:slug>/',views.DeleteCategoryAPIView.as_view(),name='delete_category_api'),
    # CRUD Movie...
    path('list_create_movie_api/',views.ListCreateMovieAPIView.as_view(),name='list_create_movie_api'),
    path('retrieve_update_delete_api/<slug:slug>/',views.RetrieveUpdateDestroyMovieAPIView.as_view(),name='retrieve_update_delete_api'),
    # List or Create Like Movies and Seryal Movie...
    path('list_create_like_movie_api/',views.ListCreateLikeMovieAPIView.as_view(),name='list_create_like_movie_api'),
    path('list_create_like_seryalmovie_api/',views.ListCreateLikeSeryalMovieAPIView.as_view(),name='list_create_like_seryalmovie_api'),
    # Comment Movies...
    path('create_list_comment_movie_api/',views.CommentMovieAPIView.as_view(),name='create_list_comment_movie_api'),
    path('retrieve_update_delete_comment_movie_api/<int:pk>/',views.RetrieveUpdateDestroyCommentMovieAPIView.as_view(),name='retrieve_update_delete_comment_movie_api'),
    # Comment Seryal Movies...
    path('create_list_comment_seryal_movie_api/',views.CommentSeryalMovieAPIView.as_view(),name='create_list_comment_seryal_movie_api'),
    path('retrieve_update_delete_comment_seryal_movie_api/<int:pk>/',views.RetrieveUpdateDestroyCommentSeryalMovieAPIView.as_view(),name='retrieve_update_delete_comment_seryal_movie_api'),
    # Views App...
    path('home_api/',views.HomeAPIView.as_view(),name='home_api'),
    path('list_ternd_movie_api/',views.ListTrendMoviesAPIView.as_view(),name='list_ternd_movie_api'),
    path('list_action_movie_api/',views.ListActionMoviesAPIView.as_view(),name='list_action_movie_api'),
    path('list_exciting_movie_api/',views.ListExcitingMoviesAPIView.as_view(),name='list_exciting_movie_api'),
    path('list_dram_movie_api/',views.ListDramMoviesAPIView.as_view(),name='list_dram_movie_api'),
    path('list_love_movie_api/',views.ListLoveMoviesAPIView.as_view(),name='list_love_movie_api'),
    path('list_scary_movie_api/',views.ListScaryMoviesAPIView.as_view(),name='list_scary_movie_api'),
    path('list_seryal_api/',views.ListSeryalsAPIView.as_view(),name='list_seryal_api'),
    path('list_category_page_api/',views.CategoryPageAPIView.as_view(),name='list_category_page_api'),
    path('filter_category_page_api/<slug:slug>/',views.FilterCategoryPageAPIView.as_view(),name='filter_category_page_api'),
    # Detail Movies...
    path('detail_movies_api/<slug:slug>/',views.DetailMoviesAPIView.as_view(),name='detail_movies_api'),
]
# CRUD Seryal Movie...
router = routers.SimpleRouter()
router.register('crud_seryal_movie_api',views.CRUD_SeryalMovieAPIView)
urlpatterns += router.urls
