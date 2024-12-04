from gc import get_objects

from django.contrib.auth import logout

from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.forms import TacheForm, TacheForm_
from posts.models import Tache, CustomUser


class TachesHome(ListView):
    model = Tache
    context_object_name = "posts"

class TachesCreate(CreateView):
    model = Tache
    form_class = TacheForm
    template_name = "posts/tache_create.html"

    def form_valid(self, form):
        form.instance.responsable = self.request.user
        return super().form_valid(form)
#

class TachesUpdate(UpdateView):
    model = Tache
    template_name = "posts/tache_edit.html"

    form_class = TacheForm_


class TachesDetail(DetailView):
    model = Tache
    context_object_name = "post"


class TachesDelete(DeleteView):
    model = Tache
    context_object_name = "post"
    success_url = reverse_lazy("posts:acceuil")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "posts/signup.html", {"error": "Les mots de passe ne colent pas"})

        CustomUser.objects.create_user(username=username, password=password1)
        return render(request,'posts/tache_list.html')
    return render(request, "posts/signup.html")


def logout_view(request):
    logout(request)
    return render(request, 'posts/signup.html')