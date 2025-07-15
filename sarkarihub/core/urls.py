from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path('latest-jobs/', views.latest_jobs, name='latest_jobs'),
    path('admit-cards/', views.admit_cards, name='admit_cards'),
    path('results/', views.results, name='results'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about/', views.about, name='about'),
    path('job/<int:post_id>/', views.job_detail, name='job_detail'),
]
