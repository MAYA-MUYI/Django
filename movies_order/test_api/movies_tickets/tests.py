import requests
import json
import re

def date_format(day):
    date_list = re.findall('\d+', str(day))
    if len(date_list) == 2:
        date_list[0] = str(int(date_list[0]))
        date_list[1] = str(int(date_list[1]))
    elif len(date_list) == 3:
        date_list = date_list[1:]
        date_list[0] = str(int(date_list[0]))
        date_list[1] = str(int(date_list[1]))
    return date_list[0] + '-' + date_list[1]






if __name__ == '__main__':
    a = ["11:45", "12:45", "12:50","13:00","11:30"]
    a.sort()
    print(a)
    print(type(a))
