# Generated by Django 4.0a1 on 2021-11-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_product_options_remove_product_is_free_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d'),
        ),
    ]
