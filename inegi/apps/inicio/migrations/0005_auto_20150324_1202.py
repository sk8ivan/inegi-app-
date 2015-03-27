# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_remove_file_idequipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parche',
            name='ParcheFecha',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
