from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('contact/', views.listing, name='listing'),
    path('article/',views.add_article,name='add_article'),
    path('s\'inscrire/',views.inscription,name='inscription'),
    path('login/',views.login,name='login'),
    path('detail/<int:article_id>',views.detail_article,name='detail_article'),


]
