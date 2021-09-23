from django.db import models

class User_compt(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    phone_Number=models.IntegerField(null=True)
    mails=models.EmailField(max_length=100)
    birthday=models.DateField()
    sex=models.IntegerChoices('M','F')
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.name+" "+self.surname


class User_profil(models.Model):
    photo_user=models.ImageField(upload_to='image_profil/')
    user_id=models.OneToOneField(User_compt,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id


class User_shop(models.Model):
    name_shop=models.CharField(max_length=100)
    description=models.TextField(max_length=255)
    categorie_shop=models.CharField(max_length=50)
    shop_date=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User_compt, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_shop


class Article(models.Model):
    article_name=models.CharField(max_length=50)
    article_type=models.CharField(max_length=100)
    article_description=models.TextField()
    article_price=models.IntegerField()
    article_quantity=models.IntegerField()
    article_date=models.DateTimeField(auto_now_add=True)
    article_available=models.BooleanField(default=True)
    user_shop_id=models.ManyToManyField(User_shop)
    article_image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.article_name
