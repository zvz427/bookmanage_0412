# *_* coding: utf-8 *_*
from django.contrib import admin
from models import Book,Author,Publisher,Userinfo
# Register your models here.

#
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
# admin.site.register(Userinfo)

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    actions_on_top = False
    actions_on_bottom = True
    ordering = ['email']
    search_fields = ['username','password','email']
    list_display = ['username','password','email']
    fields = ('password','email','username')#干什么用的?????????????????????????//