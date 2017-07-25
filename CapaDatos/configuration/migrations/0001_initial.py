# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=144)),
                ('comentarios', models.TextField()),
                ('status', models.CharField(choices=[('ERR', 'ERROR'), ('SUC', 'Exito')], default='REC', max_length=3)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_creador', to='security.Profile')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_actualizador', to='security.Profile')),
            ],
        ),
    ]
