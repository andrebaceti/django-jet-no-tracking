# Generated by Django 3.2.6 on 2023-11-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jet', '0002_delete_userdashboardmodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pinnedapplication',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
