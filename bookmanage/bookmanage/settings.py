# *_*coding: utf-8*_*
"""
Django settings for bookmanage project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""


# 图书系统项目基本要求:
# 1. 使用bootstrap 来实现登陆， 注册 、 注销功能
# 	要求：
# 		样式美观、
# 		使用mysql 存储数据
# 		在注册加入session， 在登陆校验session
#
# 2. 页面：
# 	1. 定义基础页面，使用模板的继承和块语句
# 	2.
# 		1. 要有首页， 首页展示书籍的列表
# 		2. 在列表里有超链接能够查看每个书籍的详情
# 			详情：
# 				书的名字。 书的作者、 书的价格、 出版社、出版社日期、 评论数量
# 		3. 在详情页面里有超链接能够看到输书籍的作者的信息
# 			name
# 			addree


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$z8q$d62$39er7cbx!zr&n+xn^=v_0zu596uqen+4@gby^m6#6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookquery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmanage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmanage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookquery',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'zxy',
        'PASSWORD': 'zz',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

#静态文件的目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# 使用redis　做缓存，　要变换缓存的引擎
SESSION_ENGINE = 'redis_sessions.session'
# redis 的配置文件
SESSION_REDIS_HOST = '127.0.0.1'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 1
SESSION_REDIS_PASSWORD = ''
SESSION_REDIS_PREFIX = 'session'  # 会话的开始标识

#日志系统
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, #是否
    'handlers': {
        'file': {
            'level': 'DEBUG', #日志级别
            'class': 'logging.FileHandler',
            'filename': '/home/zxy/python2_env/bookmanage/bookmanage/debug.log', # 写入本地文件，要确保文件有读写的权限
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True, # 在console是否输出
        },
    },
}
