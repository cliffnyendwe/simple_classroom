# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.files.storage
from django.db import models, migrations
import simple_classroom.apps.downloads


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_auto_20150220_2208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictation',
            options={'ordering': ['-year', 'subject'], 'verbose_name': 'Dictado', 'verbose_name_plural': 'Dictados'},
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='avatar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'avatar', null=True, verbose_name='Avatar', blank=True),
            preserve_default=True,
        ),
    ]
