# Generated by Django 3.1.4 on 2021-01-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210104_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='cart.png', null=True, upload_to=None),
        ),
    ]
