# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20150318_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='idEquipo',
        ),
    ]
