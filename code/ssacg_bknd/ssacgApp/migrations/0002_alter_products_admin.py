# Generated by Django 3.2.8 on 2021-10-11 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssacgApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Administrator', to='ssacgApp.admins'),
        ),
    ]
