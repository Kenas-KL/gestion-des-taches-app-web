from django.contrib import admin

# Register your models here.

from posts.models import Tache, CustomUser


class TacheAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "responsable", "date_de_debut", "date_de_fin", "priorite", "statut", "avancement", "commentaires",)
    list_editable = ("priorite",)


class CustomUserAdmin(admin.ModelAdmin):
     list_display = ("username", "password","is_allowed", "is_staff", "is_active")
     list_editable = ("is_staff","is_allowed", )



admin.site.register(Tache, TacheAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
