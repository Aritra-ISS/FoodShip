# Generated by Django 4.1.3 on 2022-11-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_productreview_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='review_id',
        ),
        migrations.AddField(
            model_name='productreview',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]