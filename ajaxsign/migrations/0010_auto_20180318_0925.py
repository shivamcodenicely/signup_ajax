# Generated by Django 2.0.3 on 2018-03-18 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxsign', '0009_auto_20180317_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electonics',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop_Brand',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop_Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model_number', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('laptop_model_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Laptop_Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=50)),
                ('laptop_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Electonics')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_Brand',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model_number', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('mobile_model_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Mobile_Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=50)),
                ('mobile_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Electonics')),
            ],
        ),
        migrations.AlterField(
            model_name='sign',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AddField(
            model_name='mobile_brand',
            name='mobile_brand_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Mobiles'),
        ),
        migrations.AddField(
            model_name='laptop_brand',
            name='laptop_brand_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxsign.Laptops'),
        ),
    ]