# Generated by Django 4.1.2 on 2022-11-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('address_preference', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='secondary', max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(max_length=255)),
                ('pin', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address_type', models.CharField(choices=[('home', 'home'), ('office', 'office')], max_length=255)),
            ],
        ),
    ]