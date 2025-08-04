from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/lost/', views.post_lost, name='post_lost'),
    path('post/found/', views.post_found, name='post_found'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('search/', views.search_items, name='search'),
] 