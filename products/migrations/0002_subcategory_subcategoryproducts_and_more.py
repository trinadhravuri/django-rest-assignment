# Generated by Django 5.0.6 on 2024-05-17 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('sub_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryProducts',
        ),
    ]