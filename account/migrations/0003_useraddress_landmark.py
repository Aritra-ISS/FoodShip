# Generated by Django 4.1.2 on 2022-11-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='landmark',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
