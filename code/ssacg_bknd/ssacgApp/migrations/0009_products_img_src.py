# Generated by Django 3.2.8 on 2021-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacgApp', '0008_alter_products_unitary_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img_src',
            field=models.CharField(default='Sin imágen', max_length=2083),
        ),
    ]
