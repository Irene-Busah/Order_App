# Generated by Django 4.1.2 on 2022-10-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiLib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_desc',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('1', 'Food'), ('2', 'Clothes'), ('3', 'Shoes'), ('4', 'Cosmetics'), ('5', 'Sandals'), ('6', 'Bags'), ('7', 'Accessories'), ('8', 'Other')], default='1', max_length=50),
        ),
    ]
