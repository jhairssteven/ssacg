# Generated by Django 3.2.8 on 2021-10-27 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssacgApp', '0008_alter_products_unitary_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='ssacgApp.clients'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
