# Generated by Django 4.1.4 on 2023-01-04 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_rename_hire_date_realtor_date_of_hire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='date_of_hire',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
