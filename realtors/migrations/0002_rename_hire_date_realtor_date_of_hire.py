# Generated by Django 4.1.4 on 2023-01-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hire_date',
            new_name='date_of_hire',
        ),
    ]