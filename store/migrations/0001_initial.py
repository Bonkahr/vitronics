# Generated by Django 5.0.4 on 2024-04-21 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('voltage_level', models.CharField(choices=[(12, 12), (24, 24), (48, 48), (110, 110), (220, 220), ('110 ~ 240', '110 ~ 240'), (415, 415), (1000, 1000), ('N/A', 'N/A')], max_length=20)),
                ('voltage_type', models.CharField(choices=[('AC', 'AC'), ('DC', 'DC'), ('AC & DC', 'AC & DC'), ('N/A', 'N/A')], max_length=10)),
                ('phases', models.CharField(choices=[('3-PHASE', '3-PHASE'), ('1-PHASE', '1-PHASE'), ('1 & 3 PHASE', '1 & 3 PHASE'), ('N/A', 'N/A')], max_length=20)),
                ('power', models.IntegerField()),
                ('price', models.IntegerField()),
                ('featured_product', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('photo', models.ImageField(null=True, upload_to='images/store/products_main')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/store/product')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
