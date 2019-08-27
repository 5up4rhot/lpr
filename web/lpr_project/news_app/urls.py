from django.urls import path
from . import views

app_name = 'news_app'
urlpatterns = [
    # for visitors
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug_url>',
         views.post_detail, name='post_detail'),
    path('author/<int:pk>', views.AuthorPostListView.as_view(), name='user_post_list'),

    # for staff
    path('profile', views.ProfilePostListView.as_view(), name='profile_post_list'),
    path('profile/<int:pk>', views.ProfilePostDetailView.as_view(), name='profile_post_preview'),
    path('profile/create', views.CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', views.UpdatePostView.as_view(), name='update_post'),
    path('profile/<int:pk>/delete', views.DeletePostView.as_view(), name='delete_post'),
]
