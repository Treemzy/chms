# Generated by Django 3.2.9 on 2021-11-24 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0011_alter_appointment_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patientID',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CHospital.patient'),
        ),
    ]
