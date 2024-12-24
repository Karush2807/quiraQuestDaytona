from . import views
from django.urls import path

urlpatterns = [
    path("", views.mudda_list, name='mudda_list'),
    path("create/", views.mudda_create, name='mudda_create'),
    path("<int:mudda_id>/delete/", views.del_mudda, name='del_mudda'),
    path("<int:mudda_id>/edit/", views.edit_mudda, name='edit_mudda'),
    path("register/", views.register, name='register'),
    path('search/', views.searchMudda, name='searchMudda'),  # This should match exactly
    path('like/<int:mudda_id>/', views.like_mudda, name='like_mudda'),
    path('mudda/comment/<int:mudda_id>/', views.add_comment, name='add_comment'),




] 