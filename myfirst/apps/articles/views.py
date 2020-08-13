from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from.models import Article

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http4004("Sahifa topilmadi!")
    return render(request, 'articles/detail.html', {'article':a})

    latest_comments_list = a.comment_set.order_by('-id')[:]
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http4004("Sahifa topilmadi!")
    return render(request, 'articles/detail.html', {'article': a})
    a.comment_set.create(author_name =request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )