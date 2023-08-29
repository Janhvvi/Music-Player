# Create your views here.
from django.shortcuts import render

# imported our models
from django.core.paginator import Paginator
from .models import Song,category

def genre(request,name=''):
    data=category.objects.all().values()
    category_list=dict()
    for i in data:
        j=i["name"]
        category_list[j]=i["name"]
    if name:
        paginator=Paginator(Song.objects.filter(category__name=name),1)
    else:
        paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj,"category":category_list}
    return render(request,"index.html",context)