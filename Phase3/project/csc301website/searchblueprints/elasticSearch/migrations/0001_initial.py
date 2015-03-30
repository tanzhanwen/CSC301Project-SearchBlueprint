# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchNote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
