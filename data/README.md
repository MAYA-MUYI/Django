>职位可视化分析平台

##简介
1. 项目采用Django框架进行网站架构，结合爬虫、echarts图表，wordcloud等对职位信息进行分析展示。
2. 数据来自拉勾网，采用scrapy爬虫框架获取，仅用作学习。
3. 页面采用Amaze UI | HTML5 跨屏前端框架进行设计。

##运行方式（网站运行在data目录下，数据获取在lagou__full当中）
I. 首先创建对应数据库并在settings.py中更改相应配置

II. 数据导入（两种方式）：
1. 数据库中可以直接引用contest.sql,里面包含所有数据表的信息以及数据，过程中如果出现问题可以删除除positions的所有表重新执行迁移命令
2. 表的创建可以在数据库中导入positions.sql,之后python manage.py loaddata data.json导入数据，之后执行迁移

III. 命令执行
~~~
#安装依赖
pip install -r requirements.txt

#数据表创建与迁移(已执行可跳过)
python manage.py makemigrations
python manage.py migrate

#开启服务器
python manage.py runsever

~~~
##功能详情
>平台提供用户功能，用户可以通过注册登录后进行信息浏览以及后续操作，未登录用户仅提供浏览一般职位信息，不提供搜索、详情以及更多高级功能。

###1. 用户操作

I.  注册
>注册时会验证邮箱并执行密码验证以及用户名判重等处理，注册成功后自动跳转到主页，

![注册](https://upload-images.jianshu.io/upload_images/7415868-ecf2b5ee7adf7ffd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![注册](https://upload-images.jianshu.io/upload_images/7415868-be4ca72f010a78a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

II.  登录
>登录时需要提供用户名以及密码，忘记密码可以通过邮箱找回

![登录](https://upload-images.jianshu.io/upload_images/7415868-182d8db831af2b46.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
III. 登出
>登出后自动返回主页

IV. 查看个人信息(昵称、邮箱、密码等)
>通过个人信息页面可以查看个人信息并更改/绑定邮箱，更改昵称、密码等

![用户信息](https://upload-images.jianshu.io/upload_images/7415868-33749304c27dd35f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


V. 修改/绑定邮箱
>个人信息页下方按键

![绑定邮箱](https://upload-images.jianshu.io/upload_images/7415868-4b8f8dad3abc51d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

VI.修改密码
>个人信息页下方按键

![修改密码](https://upload-images.jianshu.io/upload_images/7415868-3fa06abda7be54d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


VII. 修改昵称
>个人信息页下方按键

![修改昵称](https://upload-images.jianshu.io/upload_images/7415868-966c944245882a6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###2. 页面
I. 主页
>简单介绍整体职位概况，通过动态的薪资梯度柱状图、动态词云、职位推荐表格，岗位占比进度条以及对薪资、热门行业、岗位数量的陈列展示数据

![主页](https://upload-images.jianshu.io/upload_images/7415868-e452a4693298fdf8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

II. 图表页面
>通过岗位数量情况的城市分布情况图、城市薪资及企业规模变化年度统计图(动态)、全国各城市 薪资情况/排名图进行展示

![图表](https://upload-images.jianshu.io/upload_images/7415868-7b0e1f5862dc33d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

III. 职位展示页面
>展示所有职位，可通过下拉框选择不同分类

![职位展示](https://upload-images.jianshu.io/upload_images/7415868-925ddfe03114eff4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

IV. 职位分类
>按照职位的方向领域分类

![职位类型](https://upload-images.jianshu.io/upload_images/7415868-df949b41893b11eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

V. 职位详情
>点击数据中的任意职位可跳转到详情页，对职位的具体信息进行介绍，包括工作地址、公司、工作详情等等

![职位详情](https://upload-images.jianshu.io/upload_images/7415868-500878bb2bd59ffd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

VI. 表格页
>通过表格形式展示各类型数据

![表格](https://upload-images.jianshu.io/upload_images/7415868-7003328118203418.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


VII. 备忘页面
> 可以在备忘页面中设置相应备忘文本，届时做提醒

![备忘](https://upload-images.jianshu.io/upload_images/7415868-aeb3926c7a44cf26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

VIII. 搜索功能
>在职位展示页面以及所有页面顶部导航处都提供搜索功能，分别是方向检索以及全网检索

