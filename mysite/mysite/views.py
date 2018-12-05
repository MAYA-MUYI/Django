import datetime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import ContentType
from read_statistics.utils import  get_seven_read_data, get_today_hot_data, get_yesterday_hot_data
from blog.models import Blog


from django.utils import timezone


def get_last_week_hot_data():
    today = timezone.now().date()
    date =today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today, read_details__date__gt=date) \
                        .values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')) \
                        .order_by('-read_num_sum')
    return blogs[:5]


# def get_today_hot_data():
#     today = timezone.now().date()
#     blogs = Blog.objects.filter(read_details__date=today) \
#                         .values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')) \
#                         .order_by('-read_num_sum')
#     return blogs[:5]

# def get_yesterday_hot_data():
#     yesterday = timezone.now().date() - datetime.timedelta(days=1)
#     blogs = Blog.objects.filter(read_details__date=yesterday) \
#                         .values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')) \
#                         .order_by('-read_num_sum')
#     return blogs[:5]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_read_data(blog_content_type)
    # today_hot_data = get_today_hot_data(blog_content_type)
    # yesterday_hot_data = get_yesterday_hot_data(blog_content_type)

    last_week_hot_data = cache.get('last_week_hot_data')
    if last_week_hot_data is None:
        last_week_hot_data = get_last_week_hot_data()
        cache.set('last_week_hot_data', last_week_hot_data, 3600)
        print("*****    calc    *****")
    else:
        print("*****    use cache   *****")

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['last_week_hot_data'] = last_week_hot_data
    return render(request, 'home.html', context)
