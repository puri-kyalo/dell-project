# Generated by Django 3.2.22 on 2023-10-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=0)),
                ('productname', models.CharField(max_length=70)),
                ('productprice', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
