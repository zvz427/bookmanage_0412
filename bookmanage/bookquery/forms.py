#*_*coding= utf-8*_*

from django import forms
from django.forms import Form
from models import Userinfo
from django.forms import ValidationError

def check_name(value):
    if Userinfo.objects.filter(name=value):
        raise ValidationError('姓名已存在')
# class UserinfoForm(Form):
class UserinfoForm(forms.Form):
    name = forms.CharField(label='用户名',max_length=15,validators=[check_name])
    password = forms.CharField(label='用户密码',max_length=100)
    email =forms.EmailField(label='用户邮箱',max_length=30)

class UserinfoModelForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        exclude = ('id',)