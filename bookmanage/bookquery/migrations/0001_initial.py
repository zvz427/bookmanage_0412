# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='\u4f5c\u8005\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u4f5c\u8005\u90ae\u7bb1')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u4e66\u540d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u4ef7\u683c')),
                ('pub_date', models.DateField(verbose_name='\u51fa\u7248\u65e5\u671f')),
                ('comment', models.IntegerField(verbose_name='\u8bc4\u8bba\u6570')),
                ('author', models.ManyToManyField(to='bookquery.Author', verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u51fa\u7248\u793e\u540d\u79f0')),
                ('address', models.CharField(max_length=100, verbose_name='\u51fa\u7248\u793e\u5730\u5740')),
                ('website', models.URLField(verbose_name='\u51fa\u7248\u793e\u7f51\u5740')),
            ],
            options={
                'verbose_name': '\u51fa\u7248\u793e',
                'verbose_name_plural': '\u51fa\u7248\u793e',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookquery.Publisher', verbose_name='\u51fa\u7248\u793e'),
        ),
    ]
