# Generated by Django 4.1.7 on 2024-03-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festmgmt', '0013_alter_useracc_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
