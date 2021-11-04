# Generated by Django 3.2.8 on 2021-11-04 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(editable=False)),
                ('summary', models.TextField(max_length=255)),
                ('is_free', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.category')),
            ],
        ),
    ]
