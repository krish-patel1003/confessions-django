# Generated by Django 4.1 on 2022-08-28 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confession',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 17, 58, 9, 263388)),
        ),
    ]