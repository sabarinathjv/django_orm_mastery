# Generated by Django 3.2.7 on 2021-11-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0003_mybook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybook',
            name='cost',
            field=models.BigIntegerField(),
        ),
    ]
