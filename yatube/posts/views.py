from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group

# Create your views here.


def index(request):
    template = 'posts/index.html'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date', 'group')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author', 'group')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        'text': 'Здесь будет информация о группах проекта Yatube',
        'title': group.title,
    }
    return render(request, template, context)