from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import create_compteforms
from .models import User_shop, User_compt, User_profil, Article


def listing(request):
    # phrase='Yes'
    art = Article.objects.all()
    return render(request, 'store/garde.html', {'compte': art})


def detail_article(request,article_id):
    art = Article.objects.get(id=article_id)
    return render(request, 'store/index.html', {'compte': art})

def add_article(request):
    return  render(request, 'store/add_article.html',)
def sho_profil(request,user_id):
    user=User_compt.object.get(id=user_id)
    return render((request,'store/user_profil.html',{'user':user}))

#Création de compte par un vendeur
def inscription(request):
    if request.method=='POST':
        form=create_compteforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:profile')
        else:
            print(form.errors)
    else:
        form=create_compteforms()

    return  render(request, 'store/s\'user_profil.html',{'form':form})

def login(request):
    return render(request,'store/connexion.html',)

"""
def search(request):
    query = request.GET.get('query')
    if not query:
        art = Article.objects.all()
    else:
        art=Article.objects.filter(aricle_name_icontent=query)
"""
