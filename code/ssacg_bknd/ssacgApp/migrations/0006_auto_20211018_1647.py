# Generated by Django 3.2.8 on 2021-10-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacgApp', '0005_auto_20211018_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name=500),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
