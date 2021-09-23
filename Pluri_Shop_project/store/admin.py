import django
from django.contrib import admin

# Register your models here.
from .models import User_compt, User_profil, User_shop, Article

admin.site.register(User_compt)
admin.site.register(User_profil)
admin.site.register(User_shop)
admin.site.register(Article)
