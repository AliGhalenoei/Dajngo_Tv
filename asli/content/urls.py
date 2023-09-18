from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home'),
    path('list_ternd_movie/',views.ListTrendMoviesView.as_view(),name='list_ternd_movie'),
    path('list_action_movie/',views.ListActionMoviesView.as_view(),name='list_action_movie'),
    path('list_exciting_movie/',views.ListExcitingMoviesView.as_view(),name='list_exciting_movie'),
    path('list_dram_movie/',views.ListDramMoviesView.as_view(),name='list_dram_movie'),
    path('list_love_movie/',views.ListLoveMoviesView.as_view(),name='list_love_movie'),
    path('list_scary_movie/',views.ListScaryMoviesView.as_view(),name='list_scary_movie'),
    #Search Movies url...
    path('search/',views.SearchMoviesView.as_view(),name='search'),
    # DEtails Movies...
    path('detail/<slug:slug>/',views.DetailMoviesView.as_view(),name='detail_movies'),
    # Page Play Movie...
    path('play/<slug:slug>/',views.PlayMoviePageView.as_view(),name='play_movie'),
    # Update And Delete Comment...
    path('update_comment/<int:pk>/',views.UpdateCommentView.as_view(),name='update_comment'),
    path('delete_comment/<int:pk>/',views.DeleteCommentView.as_view(),name='delete_comment'),
    # Save And Like Movie...
    path('save/<slug:slug>/',views.SaveMovieView.as_view(),name='save'),
    path('unsave/<slug:slug>/',views.UnSaveMovieView.as_view(),name='unsave'),
    path('save_list/<int:pk>/',views.ListSaveMoviesView.as_view(),name='save_list'),
    #Like Movie...
    path('like/<slug:slug>/',views.LikeMovieView.as_view(),name='like_movie'),
    path('dislike/<slug:slug>/',views.DisLikeMovieView.as_view(),name='dislike_movie'),
    # Category Page...
    path('categorys/',views.CategoryPageView.as_view(),name='list_categorys'),
    path('filter_category/<slug:slug>/',views.FilterCategoryPageView.as_view(),name='filter_category'),
    # Contact url...
    path('contact/',views.ContactView.as_view(),name='contact'),
    # Detail Movies...
    path('detail_seryal_movies/<int:pk>/',views.DetailSeryalView.as_view(),name='detail_seryal_movies'),
    path('update_comment_seryal/<int:pk>/',views.UpdateCommentSeryalView.as_view(),name='update_comment_seryal'),
    path('delete_comment_seryal/<int:pk>/',views.DeleteCommentSeryalView.as_view(),name='delete_comment_seryal'),
    # list Seryals (navbar)...
    path('seryals/',views.ListSeryalsView.as_view(),name='seryals'),
    path('play_seryal/<int:pk>/',views.PlaySeryal.as_view(),name='play_seryal'),
    # Save And Like Seryal...
    path('save_seryal/<slug:slug>/',views.SaveSeryalView.as_view(),name='save_seryal'),
    path('unsave_seryal/<slug:slug>/',views.UnSaveSeryalView.as_view(),name='unsave_seryal'),
    path('like_seryal/<slug:slug>/',views.LikeSeryalView.as_view(),name='like_seryal'),
    path('dislike_seryal/<slug:slug>/',views.DisLikeSeryalView.as_view(),name='dislike_seryal'),

]
