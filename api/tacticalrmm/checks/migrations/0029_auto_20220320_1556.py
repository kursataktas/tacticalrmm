# Generated by Django 3.2.12 on 2022-03-20 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0028_rename_policycheckresults_policycheckresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='managed_by_policy',
        ),
        migrations.RemoveField(
            model_name='check',
            name='parent_check',
        ),
        migrations.RemoveField(
            model_name='policycheckresult',
            name='timeout',
        ),
    ]
