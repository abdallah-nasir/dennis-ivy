# Generated by Django 3.1.4 on 2021-01-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210104_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/img/pic.JPG', null=True, upload_to=None),
        ),
    ]