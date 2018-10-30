from django.shortcuts import render
from movie.models import MovieModels
# Create your views here.
def index(request,page=0):
    if page>1:
        return render(request, "index.html", context={"list": MovieModels.objects.all()[(page-1)*20:page*20], 'up': page+1})
    else:
        return render(request, "index.html", context={"list": MovieModels.objects.all()[:20]})

def movie(request,id):
    model = MovieModels.objects.get(id=id)
    return render(request, "detail.html", context={'name': model.name, 'link': model.link, 'content': model.content})