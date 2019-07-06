from django.shortcuts import render, get_object_or_404
from .tools import *
import re
import math


# Create your views here.

def calendar(request):
    context = common_Data()
    return render(request, 'positions/calendar.html', context)


def error(request):
    context = common_Data()
    return render(request, 'positions/404.html', context)


def index(request):
    context = common_Data()
    #统计顶薪
    infos = dict(Positions.objects.order_by("?").values_list('job_name', 'salary_range'))
    for k, v in infos.items():
        infos[k] = re.findall('\d+', v)[1]
    context['result'] = infos


    context['this_month_count'],context['last_month_count']  = month_count()

    if context['this_month_count'] - context['last_month_count'] > 0:
        context['changed_count'].append([1, int(math.fabs(context['this_month_count'] - context['last_month_count']))])
    else:
        context['changed_count'].append([0, int(math.fabs(context['this_month_count'] - context['last_month_count']))])

    #最高薪职业
    max, min = salary_range()
    salary_top = max[0][0]
    context['salary_top'] = salary_top
    context['salary_top_range'] = Positions.objects.filter(job_name=salary_top).values_list('salary_range')[0][0]
    salary_sum, salary_equal_cate, tmp_list = hot_cate()
    context['average_salary'] = int(float(salary_sum/len(salary_equal_cate)))
    context['hot_position'] = tmp_list[0][0]
    context['internet_rate'] = int(float(len(Positions.objects.filter(company_field__contains='移动互联网'))/len(Positions.objects.all())*100))
    context['commerce'] = int(float(len(Positions.objects.filter(company_field__contains='电子商务'))/len(Positions.objects.all())*100))
    context['other'] = 100 - context['internet_rate'] - context['commerce']
    context['words_list'] = words_cloud()
    context['today_positions'] = today_positions()

    return render(request, 'positions/index.html', context)


def tables(request):
    context = common_Data()
    context['high_salary_positions'] = high_salary_positions()[:6]
    context['company_info'] = company_info()
    city_positions = list(positions_count())
    city_positions = sorted(city_positions, key=lambda item: item[1], reverse=True)
    context['city_positions'] = city_positions[:10]
    context['cate_infos'] = salary_range_by_cate()
    context['recently_positions'] = recently_positions()
    return render(request, 'positions/tables.html', context)


def chart(request):
    context = common_Data()
    context['city_value'] = city_values()
    context['city_salary'], context['company_size'], citys = salary_with_size()
    context['citys'] = citys[:10]
    context['salary_with_city'] = city_average_salarys(citys)
    return render(request, 'positions/chart.html', context)


def positions_list(request):
    positions = Positions.objects.all()
    context = get_Common(request, positions)
    return render(request, 'positions/table-list.html', context)


def search_by_catename(request, catename):
    context = common_Data()
    positions = Positions.objects.filter(cate_name=catename).all()
    context = get_Common(request, positions)
    return render(request, 'positions/type_list.html', context)


def positions_detail(request, positions_pk):
    position = get_object_or_404(Positions, pk=positions_pk)
    context = common_Data()
    context['position'] = position
    return render(request, 'positions/form.html', context)

