from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


def news_home(request):
    news = Articles.objects.order_by("-date")
    return render(request, "news/news_home.html", {"news": news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"



class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = "news/create.html"
    form_class = ArticlesForm
    login_url = 'login'


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = "/news/"
    template_name = "news/news-delete.html"
    login_url = 'login'

@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    data = {
        "form": form,
        "error": error
    }
    return render(request, "news/create.html", data)