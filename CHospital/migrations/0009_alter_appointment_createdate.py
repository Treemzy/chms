# Generated by Django 3.2.9 on 2021-11-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0008_auto_20211123_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='createDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]