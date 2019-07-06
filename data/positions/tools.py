#!/usr/bin/env python
# -*- coding：utf-8 -*-
'''
@author: maya
@contact: 1278077260@qq.com
@software: Pycharm
@file: tools.py
@time: 2019/4/25 8:46
@desc:
'''
from django.core.paginator import Paginator
from django.conf import settings
from positions.models import Positions
import re
import random
import time


def is_this_month(date):
    if(len(re.findall('\d+', date))) == 3:
        if re.findall('\d+', date)[1] == re.findall('\d+', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))[1]:
            return True
        else:
            return False
    else:
        return True


def today_positions():
    all_positions = Positions.objects.all()
    today_positions = []
    for position in all_positions:
        if is_today(position.publish_time):
            today_positions.append(position)
    return random.sample(today_positions, 6)


def is_today(date):
    if (len(re.findall('\d+', date))) == 2:
        return True
    else:
        return False


def month_count():
    # 本月职位数量
    this_month_count = 0
    # 上月职位数量
    last_month_count = 0

    # 统计月度职位数量变化
    all_positions = list(Positions.objects.values_list('job_name', 'publish_time'))
    for position in all_positions:
        if is_this_month(position[1]):
            this_month_count += 1
        else:
            last_month_count += 1
    return this_month_count, last_month_count


def hot_cate():
    # 最热门行业
    tmp_dict = dict()
    cate_with_salary = dict(Positions.objects.values_list('cate_name', 'salary_range'))
    categorys = list(cate_with_salary.keys())
    for cate in categorys:
        tmp_dict[cate] = 0

    for data in Positions.objects.values_list('cate_name'):
        for category in categorys:
            if data[0] == category:
                tmp_dict[cate] += 1

    tmp_list = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)
    hot_position = tmp_list[0][0]
    salary_equal_cate = Positions.objects.filter(cate_name=hot_position).values_list('salary_range')
    salary_sum = 0
    for position in salary_equal_cate:
        salary_sum += int((int(re.findall('\d+', position[0])[0]) + int(re.findall('\d+', position[0])[1])) / 2)
    return salary_sum, salary_equal_cate, tmp_list


def average_salary(city):
    salary_sum = 0
    infos = Positions.objects.filter(working_city=city).values_list('salary_range')
    for info in infos:
        salary_sum += (int(re.findall('\d+', info[0])[0]) + int(re.findall('\d+', info[0])[1]))/2
    return ('%.1f'%(salary_sum/len(infos)))


def average_size(city):
    size_sum = 0
    infos = Positions.objects.filter(working_city=city).values_list('company_size')
    for info in infos:
        if info[0] is None:
            pass
        elif len(re.findall('\d+', info[0])) == 1:
            size_sum += (int(re.findall('\d+', info[0])[0]))
        else:
            size_sum += (int(re.findall('\d+', info[0])[0]) + int(re.findall('\d+', info[0])[1])) / 2
    return ('%s' % int(size_sum / len(infos)))


def cate_salary_min(cate):
    min_average = 0
    infos = Positions.objects.filter(cate_name=cate).values_list('salary_range')
    for info in infos:
        min_average += (int(re.findall('\d+', info[0])[0]))
    return ('%.1f' % (min_average / len(infos)))


def cate_salary_max(cate):
    max_average = 0
    infos = Positions.objects.filter(cate_name=cate).values_list('salary_range')
    for info in infos:
        max_average += (int(re.findall('\d+', info[0])[1]))
    return ('%.1f' % (max_average / len(infos)))


def recently_positions():
    positions_info = []
    infos = Positions.objects.values_list('job_name', 'salary_range', 'working_city', 'publish_time')
    for info in infos:
        if is_today(info[3]):
            positions_info.append([info[0], info[1], info[2], info[3]])
    return random.sample(positions_info, 8)


def salary_range_by_cate():
    infos = []
    cate_names = set(Positions.objects.values_list('cate_name'))
    all_count = len(Positions.objects.all())
    for cate in cate_names:
        infos.append([cate[0], cate_salary_max(cate[0]), cate_salary_min(cate[0]),
                      num_format((len(Positions.objects.filter(cate_name=cate[0]))/all_count))])
    return infos


def words_cloud():
    # 动态词云
    all = Positions.objects.all()
    words_list = []
    for data in all:
        words_list.append(
            [
                [data.job_name, 10],
                [data.cate_name, random.randint(1, 3)],
                [data.experience_required, random.randint(1, 3)],
                [data.job_type, random.randint(1, 3)],
                [data.job_advantage, random.randint(1, 3)],
                [data.working_city, random.randint(1, 3)],
                [data.salary_range, random.randint(1, 3)]
            ]
        )

    return words_list


def company_info():
    company_infos = []
    for data in Positions.objects.values_list('company_name', 'company_field', 'financing_status', 'company_size'):
        company_infos.append(list(data))

    return random.sample(company_infos, 8)


def num_format(num):
    tmp_num = ('%s' % (num*100))
    num_index = tmp_num.index(re.findall('[1-9]', tmp_num.split('.')[1])[0])
    return float(tmp_num[:num_index + 1])


def positions_count():
    citys = []
    all_count = len(Positions.objects.all())
    city_count = {}
    city_count['info'] = []
    all_positions = Positions.objects.values_list('working_city', 'salary_range')
    for data in all_positions:
        citys.append(data[0])

    for city in set(citys):
        city_count['info'].append([city, len(Positions.objects.filter(working_city=city)),
                                  num_format((len(Positions.objects.filter(working_city=city))/all_count)),
                                average_salary(city)])
    return city_count['info']


def high_salary_positions():
    high_salary_positions = []
    max_salary, min_salary = salary_range()
    for data in max_salary:
        # position_info = Positions.objects.filter(job_name=data[0]).values_list('job_name', 'salary_range', 'working_city', 'education_required')
        position_info = Positions.objects.filter(job_name=data[0])[0]
        high_salary_positions.append(position_info)
    return high_salary_positions


def salary_range():
    positions = []
    positions_max = []
    salary_min = []
    salary_max = []
    # 统计底薪
    infos = Positions.objects.values_list('job_name', 'salary_range')
    for info in infos:
        # 职位
        positions.append(info[0])
        # 底薪
        salary_min.append(int(re.findall('\d+', info[1])[0]))
        salary_max.append(int(re.findall('\d+', info[1])[1]))
    salary_max_range = sorted(dict(zip(positions, salary_max)).items(), key=lambda item: item[1], reverse=True)
    salary_min_range = sorted(dict(zip(positions, salary_min)).items(), key=lambda item: item[1], reverse=True)
    return salary_min_range, salary_max_range


def city_salary_size(citys):
    salary_infos = []
    size_infos = []
    for data in citys[:10]:
        salary_infos.append(
            int(random.randint(int(float(average_salary(data))) - 5, int(float(average_salary(data))) + 5))
            # average_salary(data)
        )
        size_infos.append(
            int(random.randint(int(float(average_size(data))), int(float(average_size(data))*1.5)))
            # average_size(data)
        )
    return salary_infos, size_infos


def salary_with_size():
    citys = []
    salary_infos = []
    size_infos = []
    infos = sorted(positions_count(), key=lambda item: item[1], reverse=True)
    for data in infos:
        citys.append(data[0])

    for i in range(12):
        salary_infos.append([city_salary_size(citys)[0]])
        size_infos.append([city_salary_size(citys)[1]])
    return salary_infos, size_infos, citys


def city_values():
    values = []
    for data in positions_count():
        if data[1] < 199:
            data[1] = 150
        values.append([data[0], data[1]])
    return values


def city_average_salarys(citys):
    salarys_with_citys = []
    for city in citys:
        salarys_with_citys.append([city, average_salary(city)])
    return salarys_with_citys


def get_Common(request, positions):
    paginator = Paginator(positions, settings.EACH_PAGE_POSITIONS_NUMBER)
    page_num = request.GET.get('page', 1)# 获取url的页面参数（GET请求）
    page_of_positions = paginator.get_page(page_num)#page_num页面对象
    current_page_num = page_of_positions.number# 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    # return page_of_positions.object_list, page_of_positions, page_range
    context['positions'] = page_of_positions.object_list
    context['page_of_positions'] = page_of_positions
    context['page_range'] = page_range
    context['cates'] = cates()
    return context


def cates():
    list_cates = []
    cates = []
    infos = Positions.objects.values_list('cate_name')
    for data in set(infos):
        list_cates.append(data[0].replace('/', ''))

    num_list = list(range(1, len(list_cates)+1))
    cates = list(zip(num_list, list_cates))
    return cates

def common_Data():
    context = {}
    context['cates'] = cates()
    # 职位数量变化
    context['changed_count'] = []
    # 今日热门职业
    context['today_hot'] = []
    return context