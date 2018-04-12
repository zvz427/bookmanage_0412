# *_*coding: utf-8*_*

from __future__ import unicode_literals

from django.db import models

# Create your models here.

#定义书籍的数据表
class Book(models.Model):
    name = models.CharField(max_length=20,verbose_name='书名')
    author = models.ManyToManyField('Author',verbose_name='作者')
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')
    publisher = models.ForeignKey('Publisher',verbose_name='出版社')
    pub_date = models.DateField(verbose_name='出版日期')
    comment = models.IntegerField(verbose_name='评论数')

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

#定义书籍出版社的数据表
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社名称')
    address = models.CharField(max_length=100,verbose_name='出版社地址')
    website = models.URLField(verbose_name='出版社网址')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

#定义书籍作者的数据表
class Author(models.Model):
    name = models.CharField(max_length=12,verbose_name='作者名')
    email = models.EmailField(verbose_name='作者邮箱')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

# 定义用来存储用户注册的数据表
class Userinfo(models.Model):
    username = models.CharField(max_length=12,verbose_name='注册用户',unique=True)
    password = models.CharField(max_length=50,verbose_name='用户密码')
    email = models.EmailField(verbose_name='注册邮箱',unique=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = '用户注册信息'
        verbose_name_plural = verbose_name