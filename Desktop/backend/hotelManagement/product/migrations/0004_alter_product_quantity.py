# Generated by Django 4.1 on 2022-11-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default="0"),
        ),
    ]
