# Generated by Django 3.2.9 on 2021-11-24 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0010_alter_appointment_patientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='createDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]