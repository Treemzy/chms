# Generated by Django 3.2.9 on 2022-01-08 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0016_auto_20220108_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispensedrugs',
            name='createDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='createDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='drugsrecord',
            name='createDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
