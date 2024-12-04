from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom utilisateur.")
        username = self.model.normalize_username(username)
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_allowed = True
        user.save()
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length= 50,
        blank=False
    )
    is_staff = models.BooleanField(default=False)
    is_allowed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class Tache(models.Model):
    title = models.CharField(max_length=150, unique = True, verbose_name="Tache")
    responsable = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    date_de_debut = models.DateField()
    date_de_fin = models.DateField(blank=True, null=True)
    priorite = models.CharField(max_length=20, choices=[
        ('absolue', 'Absolue'),
        ('haute', 'Haute'),
        ('moyenne', 'Moyenne'),
        ('basse', 'Basse'),
    ])
    statut = models.CharField(max_length=20)
    avancement = models.IntegerField(default=0)
    commentaires = models.TextField()

    class Meta:
        ordering = ['-date_de_debut']
        verbose_name = "Tache"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:acceuil')


