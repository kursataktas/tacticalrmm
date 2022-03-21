# Generated by Django 3.2.12 on 2022-03-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0029_auto_20220320_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='policycheckresult',
            name='alert_severity',
            field=models.CharField(blank=True, choices=[('info', 'Informational'), ('warning', 'Warning'), ('error', 'Error')], default='warning', max_length=15, null=True),
        ),
    ]
