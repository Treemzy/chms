# Generated by Django 3.2.9 on 2021-11-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superadmin',
            field=models.BooleanField(default=False, verbose_name='Super Admin'),
        ),
    ]
