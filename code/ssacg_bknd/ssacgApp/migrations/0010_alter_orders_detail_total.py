# Generated by Django 3.2.8 on 2021-10-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacgApp', '0009_auto_20211026_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_detail',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=11, null=True),
        ),
    ]
