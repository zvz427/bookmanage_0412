# *_*coding: utf-8*_*
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from models import Book,Author,Publisher,Userinfo
import hashlib

from django.http import HttpResponse
from forms import UserinfoForm,UserinfoModelForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

#首页判断session中是否有信息,查询到所有的书籍列表并显示
def index(request):
    # name = request.POST.get('username','游客')
    name = request.session.get('name','游客')

    # 1.不使用翻页,首页全部展示信息
    # books = Book.objects.all()
    # context = {
    #     'books':books,
    #     'name':name,
    #            }
    # return render(request,'bookquery/index.html',context=context)

    # 2.使用翻页首页每页展示4条记录
    allbook = Book.objects.all()
    book_obj = Paginator(allbook,4)
    current_page = request.GET.get('page',1)
    books = book_obj.page(number=current_page)
    context = {'books':books,'name':name,}
    return render(request,'bookquery/index.html',context=context)


def not_found(request,error):
    context = { 'error':error }
    return render(request, 'bookquery/not_found.html', context=context)

#登录界面的用户名和密码判断
def login(request):
    pwd_mysql = ''
    #得到用户POST传进来的用户名和密码
    name_client = request.POST['username']
    pwd_client = request.POST['password']
    pwd_client =hashlib.sha1(pwd_client.encode("utf-8")).hexdigest()
    # 根据传进来的用户名,把对应的信息从SQL表取出来,进行用户名和密码的判断
    try:
        user_current = Userinfo.objects.get(username=name_client)
    except Exception as e:
        print(e)
        print('没有找到此人,账号不存在!')
        return redirect(reverse('bookquery:not_found',args=['账号不存在的!']))
        # return render(request,'bookquery/not_found.html')改进更新,参数传递错误信息
    else:
        name_mqsql = user_current.username
        pwd_mysql = user_current.password
    if pwd_client == pwd_mysql:
        request.session['name'] = name_mqsql
    else:
        print('账号的密码错误!')
        return redirect(reverse('bookquery:not_found', args=['密码错误!']))
        # return render(request, 'bookquery/not_found.html')改进更新,参数传递错误信息
    return redirect(reverse('bookquery:index'))

#注销退出,把保存在session的信息删除,重复删除时不会报错.并重定向到首页
def logout(request):
    # print(request.session['name'])
    try:
        del request.session['name']
    except Exception as e:
        print('已退出')
    return redirect(reverse('bookquery:index'))

# 跳转到注册页面
def register(request):
    return render(request,'bookquery/register.html')

#保存用户的注册信息,并写入到session中,注册完成后返回首页
def register_save(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    print(username,password,email)
    #把注册的用户信息添加到mysql中
    #将密码加密存储
    password = hashlib.sha1(password.encode("utf-8")).hexdigest()
    create_temp = Userinfo.objects.create(username=username,password=password,email=email)
    #同时把当前注册的信息写入到session中(同时保存用户名和密码?????????????)
    request.session['name'] = request.POST.get('username')
    request.session['password'] = request.POST.get('password')
    print(create_temp,type(create_temp))
    return redirect(reverse('bookquery:index'))

# 得到出版社的名字,然后从数据库中查出此出版社的信息
def book_pub(request,name):
    pub = Publisher.objects.get(name=name)
    context = {'pub':pub}
    return render(request,'bookquery/publisher_info.html',context=context)

#得到书的名字,从数据库中查出此书的信息
def book_info(request,name,operate):
    book = Book.objects.get(name=name)
    # 1/得到的是作者的查询集,可以循环遍历出来,2个语句作用相同,一本书多个作者时不会报错
    author = Book.objects.get(name=name).author.all()
    # author = Author.objects.filter(book__name=book.name)

    # 2/多对多的查询,从书的名字查询到此书的作者,filter把第一项取出来,
    # author = Author.objects.filter(book__name=book.name)[0]

    # 3/多对多查询,直接从书的名字取出作者,只能取出一个人,有两个作者时报错
    # author = Author.objects.get(book__name=book.name)

    print(author)
    context = {'book':book,'author':author}
    # 根据index.html返回的参数信息选择返回的渲染页面
    if operate == 'query':
        return render(request,'bookquery/book_info.html',context=context)
    elif operate == 'update':
        return render(request,'bookquery/book_update.html',context=context)

# 修改图书信息(同book_info)-------考虑和图书信息显示页面整合,根据请求return不同页面
#                                优化后与book_info合并,根据index.html返回的参数信息选择返回的渲染页面
# def book_update(request,name):
#     book = Book.objects.get(name=name)
#     author = Book.objects.get(name=name).author.all()
#     context = {'book':book,'author':author}
#     return render(request,'bookquery/book_update.html',context=context)

#保存修改的图书信息
def save_book_update(request,update_book):
    bookname = request.POST.get('bookname')#考虑前端输入过来的数据为空,或者,不符合要求?????????????
    bookprice = request.POST.get('bookprice')
    bookdate = request.POST.get('bookdate')
    bookcomment = request.POST.get('bookcomment')
    # 用get的然后更新数据会报错!!!!!!!
    # Book.objects.get(name=update_book).update(name=bookname,price=bookprice,pub_date=bookdate,comment=bookcomment)
    try:
        Book.objects.filter(name=update_book).update(name=bookname,price=bookprice,pub_date=bookdate,comment=bookcomment)
    except Exception as e:
        print(e)
        #信息填写不全时如何处理?????????????????????-------------------------------
        # return redirect(reverse('bookquery:book_update',args=['']))

    return redirect(reverse('bookquery:index'))

# 得到作者的名字,从数据库从查出此人的信息
def author_info(request,name):
    author = Author.objects.get(name=name)
    context = {'author':author}
    return render(request,'bookquery/author_info.html',context=context)

#新增加的登录模版
def login_new(request):
    return render(request,'bookquery/login_new.html')




#csrf跨站攻击验证试验
def test(request):
    return render(request,'bookquery/csrf_test.html')
def re(request):
    name = request.POST.get('username','none')
    return render(request,'bookquery/csrf_test_show.html',{'name':name})

#django的form表单
def form_register(request):
    # 1.使用forms.Form校验数据
    # userinfo = UserinfoForm()

    # 2.使用forms.ModelForm校验数据
    userinfo = UserinfoModelForm()

    return render(request,'bookquery/form_register.html',{'userinfo':userinfo})

def form_register_hander(request):
    # 1.使用forms.Form校验数据
    user = UserinfoForm(request.POST)
    print(user,type(user))
    if user.is_valid():
        name = user.cleaned_data['name']
        password = user.cleaned_data['password']
        email = user.cleaned_data['email']
        Userinfo.objects.create(username=name,password=password,email=email)
        return HttpResponse('添加成功')
    else:
        return HttpResponse('添加失败')


    # 2.使用forms.ModelForm校验数据
    # user = UserinfoModelForm(request.POST)
    # print(user,user.is_valid())
    # if user.is_valid():
    #     user.save()
    #     return HttpResponse('添加成功')
    # else:
    #     return HttpResponse('添加失败')


#分页
def page_handler(request):
    page_data = Userinfo.objects.all()
    page_obj = Paginator(page_data,2)
    # if request.POST.get('page_num'):
    #     current_page_num = request.POST.get('page_num')
    # 跳转制定页面无法实现
    # if page_num:
    #     current_page_num = int(page_num)

        #得到从网页点击传回来的数据,数据格式以?分隔,?page=2,得到page传过来的参数
    current_page_num = request.GET.get('page',1)#当前的页数

    show_page = page_obj.page(number=current_page_num)
    return render(request,'bookquery/pageshow.html',{'show_page':show_page})

#修改书籍页面的详情信息
