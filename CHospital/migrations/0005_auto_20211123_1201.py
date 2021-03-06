# Generated by Django 3.2.9 on 2021-11-23 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0004_alter_patient_hopitalno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='createDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='creator',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
