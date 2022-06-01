# Generated by Django 3.2.9 on 2022-01-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CHospital', '0017_auto_20220108_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='patientID',
        ),
        migrations.AddField(
            model_name='dispensedrugs',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CHospital.prescription'),
        ),
    ]
