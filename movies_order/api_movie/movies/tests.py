from django.test import TestCase

# Create your tests here.

import requests
import json
if __name__ == '__main__':
    r = requests.get("http://127.0.0.1:8000/movies/")
    data = json.loads(r.text)
    print(type(data))
    name  = []
    # for i in data:
    #     name.append(i['city_name'])

    print(data)