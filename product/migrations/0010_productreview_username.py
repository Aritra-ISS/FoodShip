# Generated by Django 4.1.3 on 2022-11-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_added_on_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]