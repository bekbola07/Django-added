
from django.shortcuts import render
from .models import New, Category
from django.views.generic import DetailView
# Create your views here.
def home (request):
    first_news=New.objects.first()
    three_news=New.objects.all()[1:4]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news
})

def all_news (request):
    all_news=New.objects.all()
    return render(request,  'all-news.html',  {
        'all_news': all_news
})

class Detail_page (DetailView):
    model =New
    template_name = 'detail.html'
    context_object_name = 'news '