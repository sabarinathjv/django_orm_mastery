# Generated by Django 3.2.7 on 2021-11-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_book_cupboard_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
