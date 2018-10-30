from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from book.models import BookHome, BookDetail


def index(request):
    home_info = BookHome.objects.filter().order_by("?")[:4]
    # home_info = BookHome.objects.all()[:4]
    context = {
            "home_infos": home_info

     }
    return render(request, "home.html", context=context)
def index2(request,page=0):
    if page>0:
        return render(request, "home.html", context={"home_infos": BookHome.objects.all()[(page-1)*4:page*4], 'up': page+1})
    else:
        return render(request, "home.html", context={"home_infos": BookHome.objects.all()[:4]},)

def books(request, book_id):
    homes = BookHome.objects.get(id=book_id)
    book_info = BookDetail.objects.get(book_name=homes.book_name)
    print(book_info)
    context = {
        "book_infos": book_info
     }
    return render(request, "detail.html", context=context)

# def catalog(request, page=0):
#     page = int(page)
#     if page > 1:
#         return render(request, "home.html", context={"home_infos": BookHome.objects.all()[(page-1)*4:page*4]})
#     else:
#         return render(request, "home.html", context={"home_infos": BookHome.objects.all()[:4]})