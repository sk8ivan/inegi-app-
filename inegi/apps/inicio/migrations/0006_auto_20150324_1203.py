# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20150324_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parche',
            name='fechaAviso',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parche',
            name='fechaInstalacion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
