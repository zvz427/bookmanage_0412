# *_*coding: utf-8*_*
from django.conf.urls import url,include
import views
urlpatterns = [
    # 使用新的登录模版
    url(r'^login_new/$', views.login_new, name='login_new'),
    # 优化界面,登录失败后显示错误信息
    url(r'^not_found/(?P<error>.*)/$', views.not_found, name='not_found'),

    #首页的路由
    url(r'^index/$', views.index,name='index'),
    #登录的路由
    url(r'^login/$',views.login,name='login'),
    #注销退出的路由
    url(r'^logout/$', views.logout, name='logout'),
    #用户注册的路由
    url(r'^register/$', views.register, name='register'),
    #保存用户注册的用户名和密码到mqsql
    url(r'^register_save/$', views.register_save, name='register_save'),
    #显示书籍出版社的路由
    url(r'^index/book_pub/(?P<name>.*)/$', views.book_pub, name='book_pub'),

    # url(r'^index/(?P<book>.*)/(?P<name>.*)/$', views.book_pub, name='book_pub'),
    #每本书籍信息的路由
    url(r'^index/book_info/(?P<name>.*)/(?P<operate>.*)/$', views.book_info, name='book_info'),
    #作者信息的路由
    url(r'^index/author_info/(?P<name>.*)/$', views.author_info, name='author_info'),
    # 修改图书信息(优化后与book_info合并,根据index.html返回的参数信息选择返回的渲染页面)
    # url(r'^index/book_update/(?P<name>.*)/$', views.book_update, name='book_update'),
    #保存更改的图书信息
    url(r'^index/save_book_update/(?P<update_book>.*)/$', views.save_book_update, name='save_book_update'),








    #csrf跨站攻击验证
    url(r'^test/$', views.test,),
    url(r'^re/$', views.re,),

    #form 表单使用
    url(r'^form_register/$', views.form_register),
    url(r'^form_register_hander/$', views.form_register_hander),

    #翻页
    url(r'^page_handler/$', views.page_handler),
    # 跳转制定页面无法实现?????????????????????????????????????????????
    # url(r'^page_handler/(?P<page_num>.*)/$', views.page_handler,name='page_handler'),

]
