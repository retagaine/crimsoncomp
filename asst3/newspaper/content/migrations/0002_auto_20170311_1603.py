# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Content')),
            ],
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=' ', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributor',
            name='first_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributor',
            name='last_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
