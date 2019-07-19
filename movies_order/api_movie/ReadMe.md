# movies_api

网络电影票购票平台综合信息接口(Movie Tickets Information API)  
实时查询国内电影购票平台场次，票价等信息。   
---

## V0.1
* 基于Python Django
* 使用scrapy获取信息
* 按城市-影院-场次-票价分层查询

##1. 流程
>选择影片-> 查看详细 -> 选择影院 -> 选择位置 -> 确认支付 -> 返回订单

#2. 接口简介
###2.1. 获取电影列表
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

###2.2 获取电影详情信息

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




###2.3 获取电影院列表

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


###2.4 获取订单基础信息

>__GET cinemas/movie_base_id/cinema_id__

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


###3.7用户页面


##4. 项目运行方式

~~~
git clone ......
cd test_api
python manage.py runserver

cd ../api_movie
python manage.py runserver 3000


~~~