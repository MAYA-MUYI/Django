# movies_api

> __网络电影票购票平台综合信息接口(Movie Tickets Information API)__
> __实时查询国内电影购票平台场次，票价等信息。__

---

## V0.1
* 基于Python Django
* 使用scrapy、requests获取三家信息
* 异步处理，缓存加速
* 按城市-影院-场次-票价分层查询

##1. 流程
>__选择影片-> 查看详细 -> 选择影院 -> 选择位置 -> 确认支付 -> 返回订单__

#2. 接口简介
###2.1. [获取所有电影列表](http://127.0.0.1:8000/movies)
>__URL : GET /movies/__

__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "movie_base_id": 1,
        "movie_name": "5月天诺亚方舟",
        "time": "2013-09-19",
        "star": 8.8,
        "vision": "3D",
        "ellipsis": "Mayday nowhere 3D",
        "type": "科幻,灾难,动作",
        "pic": "image/5月天诺亚方舟_pic.jpg",
        "ellipsis_length": 17
    },
    {
        "movie_base_id": 2,
        "movie_name": "厉鬼将映",
        "time": "2008-10-30",
        "star": 9.1,
        "vision": "",
        "ellipsis": "โปรแกรมหน้า วิญญาณอาฆาต",
        "type": "动画,动作,冒险",
        "pic": "image/厉鬼将映_pic.jpg",
        "ellipsis_length": 23
    },
    ......
~~~

__II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| movie_base_id | int | 电影ID |
| movie_name    | string      | 电影名     |
| time    | string      | 上映时间     |
| star    | string      | 评分     |
| vision| string      |  维度    |
| ellipsis    | string      | 缩写     |
| type    | string      | 类型     |
| pic    | string      | 图片     |
| ellipsis_length    | int      | 缩写长度     |

###2.2 [获取电影详情信息](http://127.0.0.1:8000/movies/3)

>__Get movies/movie_id__

__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "movie_detail_id": 10,
        "movie_base_id": 1,
        "movie_name": "5月天诺亚方舟",
        "time": "2013-09-19",
        "star": 9.0,
        "type": "纪录片,音乐",
        "vision": "3D",
        "ellipsis": "Mayday nowhere 3D",
        "ellipsis_length": 17,
        "duration": "114",
        "introduction": "2011年，首部华人3D音乐电影《五月天追梦3DNA》公映并受到影迷热捧，两年后的新作《诺亚方舟》除了仍采用3D技术拍摄，影片将重现五月天演唱会的狂欢画面，满场歌迷手持蓝色荧光棒，仿佛置身蓝色海洋，更有歌迷激动落泪，让人身临其境体验到五月天现场演唱的魅力与氛围。该片随着五月天诺亚方舟世界巡回演唱会重生场的举行而展开拍摄，相信音乐表示，歌迷的感动以及过去两年的经历，也透过镜头记录在画面里面，希望歌迷可以通过电影重温感动。",
        "timg": "image/5月天诺亚方舟_timg.jpg",
        "pic": "image/5月天诺亚方舟_pic.jpg",
        "stills1": "image/5月天诺亚方舟_stills1.jpg",
        "stills2": "image/5月天诺亚方舟_stills2.jpg",
        "stills3": "image/5月天诺亚方舟_stills3.jpg",
        "stills4": "image/5月天诺亚方舟_stills4.jpg"
    }
]
~~~

__II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| movie_detail_id | int | 电影详情页ID |
| movie_base_id | int | 电影ID |
| movie_name | string | 电影名 |
| time | string | 上映时间 |
| star | string | 评分 |
| type | string | 类型 |
| vision | string | 维度 |
| ellipsis | string | 缩写 |
| duration | string | 电影时间 |
| introduction | string | 电影简介 |
| introduction | string | 电影简介 |
| timg| string | 封面 | 
| pic | string | 缩略图 |
| stills1 | string | 剧照 |




###2.3 [获取所有电影院列表](http://127.0.0.1:8000/movies/3/allCinemas)

>__GET cinemas/movie_id__

__I. 查看成功响应信息__

~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "cinema_id": 1,
        "cinema_name": "保利万和国际影城(都江堰店)",
        "movie_base_id": 1,
        "movie_name": "5月天诺亚方舟",
        "city": "成都",
        "address": "都江堰市彩虹大道南段295号（22点后请走斯维登公寓电梯）",
        "price": "28",
        "distance": 13.77
    },
    {
        "cinema_id": 2,
        "cinema_name": "天智创客影城(川外店)",
        "movie_base_id": 1,
        "movie_name": "5月天诺亚方舟",
        "city": "成都",
        "address": "都江堰市大观镇高尔夫大街367号四川外国语大学成都学院33栋百汇园4楼",
        "price": "30",
        "distance": 17.77
    },
    ......
~~~

 __II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| cinema_id | int | 电影院ID |
| cinema_name    | string      | 电影院名     |
| movie_base_id    | int      | 电影名     |
| city    | string      | 城市名     |
| address| string      |  电影院地址    |
| price    | string      | 电影院最低价格     |
| distance    | string      | 电影院距离     |


###2.4 [获取电影院详情信息](http://127.0.0.1:8000/movies/3/cinemasDetail/cinema_id=1)

>__GET movies/movie_base_id/cinemasDetail/cinema_id__

__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "movie_id": "1",
        "movie_name": "5月天诺亚方舟",
        "vision": "3D",
        "cinema_id": "1",
        "cinema_name": "保利万和国际影城(都江堰店)",
        "time": "09-19",
        "price": "28",
        "duration": "114"
    }
~~~

__II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| movie_id | int | 电影ID |
| movie_name    | string      | 电影名     |
| vision    | int      | 电影缩写     |
| cinema_id    | string      | 电影院id     |
| cinema_name| string      |  电影院名字    |
| time    | string      | 上映时间     |
| price    | string      | 价格     |
| duration    | string      | 电影长度     |

###2.5 [获取电影院场次接口](http://127.0.0.1:8000/movies/3/cinemaSession/cinema_name=%E4%BF%9D%E5%88%A9%E4%B8%87%E5%92%8C%E5%9B%BD%E9%99%85%E5%BD%B1%E5%9F%8E(%E9%83%BD%E6%B1%9F%E5%A0%B0%E5%BA%97))
__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "cinema_id": 15,
        "cinema_name": "CGV影城(温江店)",
        "movie_name": "哥斯拉2：怪兽之王",
        "movie_base_id": 3,
        "vision": "3DIMAX",
        "duration": "132",
        "price": "24",
        "date_list": [
            "6-4",
            "6-5"
        ],
        "movie_session": [
            [
                {
                    "date": "6-4",
                    "session_result": [
                        {
                            "date": "6-4",
                            "begin_time": "11:45",
                            "end_time": "13:57散场",
                            "lang": "英语3D",
                            "hall": "儒风酒店厅（4K双机激光）"
                        },
                        {
                            "date": "6-4",
                            "begin_time": "12:05",
                            "end_time": "14:17散场",
                            "lang": "英语3D",
                            "hall": "激光5厅"
                        },
~~~

 __II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| cinema_id | int | 电影院ID |
| cinema_name    | string      | 电影院名     |
| movie_base_id    | int      | 电影名     |
| price    | string      | 电影院最低价格     |
|  vision| string | 维度|
|  duration| string | 电影长度|
|date_list  | list | 场次时间列表 |
|  movie_session| json | 场次信息 |
|  other_day| json | 非当日场次信息 |


###2.6 [所有电影院信息](http://127.0.0.1:8000/cinemas)
__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "cinema_id": 1,
        "cinema_name": "保利万和国际影城(都江堰店)",
        "city": "成都",
        "address": "都江堰市彩虹大道南段295号（22点后请走斯维登公寓电梯）",
        "price": "28",
        "distance": 13.77
    },
    {
        "cinema_id": 2,
        "cinema_name": "天智创客影城(川外店)",
        "city": "成都",
        "address": "都江堰市大观镇高尔夫大街367号四川外国语大学成都学院33栋百汇园4楼",
        "price": "30",
        "distance": 17.77
    },
~~~

 __II. 响应参数说明__

| name | type | value |
| :---: | :----: | :----: |
| cinema_id | int | 电影院ID |
| cinema_name  | string      | 电影院名     |
| city| string      | 城市     |
| price | string      | 电影院最低价格     |
| addrss |  string| 地址 |
| distance| string | 距离 |


##2.7 某电影院某天的所有场次
__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "cinema_name": "保利万和国际影城(都江堰店)",
        "cinema_session": [
            {
                "movie_name": "哥斯拉2：怪兽之王",
                "star": "8.5",
                "result": [
                    [
                        {
                            "date": "6-4",
                            "session_result": [
                                {
                                    "date": "6-4",
                                    "begin_time": "12:00",
                                    "end_time": "14:12散场",
                                    "lang": "英语3D",
                                    "hall": "6号激光厅（影厅冠名招商中）"
                                },
                                {
                                    "date": "6-4",
                                    "begin_time": "12:45",
                                    "end_time": "14:57散场",
                                    "lang": "英语3D",
                                    "hall": "5号激光厅（影厅冠名招商中）"
                                },
~~~

 __II. 响应参数说明__
 
| name | type | value |
| :---: | :----: | :----: |
| cinema_name    | string      | 电影院名     |
| cinema_session| json| 场次信息    |

##2.8 
__I. 查看成功响应信息__
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "cinema_name": "保利万和国际影城(都江堰店)",
        "cinema_session": [
            {
                "movie_name": "哥斯拉2：怪兽之王",
                "star": "8.5",
                "today_session": [
                    {
                        "date": "6-4",
                        "begin_time": "12:00",
                        "end_time": "14:12散场",
                        "lang": "英语3D",
                        "hall": "6号激光厅（影厅冠名招商中）"
                    },
                    {
                        "date": "6-4",
                        "begin_time": "12:45",
                        "end_time": "14:57散场",
                        "lang": "英语3D",
                        "hall": "5号激光厅（影厅冠名招商中）"
                    },
                    {
                        "date": "6-4",
                        "begin_time": "13:45",
                        "end_time": "15:57散场",
                        "lang": "英语3D",
                        "hall": "3号按摩椅厅（影厅冠名招商中）"
                    },
~~~

 __II. 响应参数说明__
 
 
| name | type | value |
| :---: | :----: | :----: |
| cinema_id | int | 电影院ID |
| cinema_name    | string      | 电影院名     |
| city| string      | 城市     |
| price    | string      | 电影院最低价格     |

##2.9 
__I. 查看成功响应信息__

 __II. 响应参数说明__
 
| name | type | value |
| :---: | :----: | :----: |
| cinema_name    | string      | 电影院名     |
| cinema_session| json| 场次信息|
| today_session| json| 当日场次     |

##2.10 [获取订单信息](http://127.0.0.1:8000/order/3/1/05-31/14:20/16:32/6%E5%8F%B7%E6%BF%80%E5%85%89%E5%8E%85%EF%BC%88%E5%BD%B1%E5%8E%85%E5%86%A0%E5%90%8D%E6%8B%9B%E5%95%86%E4%B8%AD%EF%BC%89/%E8%8B%B1%E8%AF%AD3D/6-12/31_32)

__I. 查看成功响应信息__

>__GET order/__

~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "movie_name": "哥斯拉2：怪兽之王",
        "seats": "11排3座",
        "price": 28,
        "time": "6月4日 16:05",
        "vision": "3DIMAX",
        "end": "18:05",
        "hall": "5号激光厅",
        "lang": "英语3D",
        "duration": "132",
        "cinema_name": "保利万和国际影城(都江堰店)",
        "address": "都江堰市彩虹大道南段295号（22点后请走斯维登公寓电梯）",
        "introduction": "随着《哥斯拉》和《金刚：骷髅岛》在全球范围内的成功，华纳兄弟影片公司和传奇影业联手开启了怪兽宇宙系列电影的新篇章—一部史诗级动作冒险巨制。在这部电影中，哥斯拉将和众多大家在流行文化中所熟知的怪兽展开较量。全新故事中，研究神秘动物学的机构“帝王组织”成员将勇敢直面巨型怪兽，其中强大的哥斯拉也将和魔斯拉、拉顿和它的死对头——三头王基多拉展开激烈对抗。当这些只存在于传说里的超级生物再度崛起时，它们将展开王者争霸，人类的命运岌岌可危……",
        "pic": "image/哥斯拉2：怪兽之王_pic.jpg",
        "timg": "image/哥斯拉2：怪兽之王_timg.jpg",
        "date": "6-4"
    }
]
~~~

__II. 请求参数__

| name | type | value |
| :---: | :----: | :----: |
| movie_base_id| int| 电影ID    |
| cinema_id| int| 电影院ID     |
| time| int| 播放时间  |
| begin| int| 开始时间   |
| end| int| 散场时间     |
| hall| int| 放映厅     |
| lang| int| 语言     |
| date| int| 日期     |
| seats_num | string| 座位数字|

__III. 响应参数__

| name | type | value |
| :---: | :----: | :----: |
| movie_name| int| 电影名字    |
| seats| int| 座位     |
| price| string      | 票价|
| time| string      | 播放时间|
| vision| string      | 维度|
| end| string      | 散场时间|
| hall| string      | 放映厅|
| lang| string      | 语言|
| duration| string      | 电影长度|
| cinema_name| string      | 电影院名字|
| address| string      | 电影院地址|
| introduction| string | 介绍
| date | string | 日期

##2.11 注册用户


###2.12 [注册用户](http://127.0.0.1:3000/api-user-access-control/users/)
![image.png](https://upload-images.jianshu.io/upload_images/7415868-2d601851b9d2c35a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##2.13 查看用户

![image.png](https://upload-images.jianshu.io/upload_images/7415868-caf2b118d8796d02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2.14 用户具体信息
![image.png](https://upload-images.jianshu.io/upload_images/7415868-5f39359b07479a16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2.15 用户登录验证
![image.png](https://upload-images.jianshu.io/upload_images/7415868-af3cdb39a4b45014.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##3. 页面
###3.1 主页（查看电影）

![image.png](https://upload-images.jianshu.io/upload_images/7415868-bddc7d368ffa1f09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###3.2 电影详情页

![image.png](https://upload-images.jianshu.io/upload_images/7415868-f6e3177323b50008.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###3.3 影院选择页面

![image.png](https://upload-images.jianshu.io/upload_images/7415868-02292d2d38084fa4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###3.4 场次选择页面

![image.png](https://upload-images.jianshu.io/upload_images/7415868-d57989d73fd6bc09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###3.5 座位选择页面

![image.png](https://upload-images.jianshu.io/upload_images/7415868-69d8b0f0c8238b09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###3.6 订单返回页面
![image.png](https://upload-images.jianshu.io/upload_images/7415868-0c174d3ac5a2cc19.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

