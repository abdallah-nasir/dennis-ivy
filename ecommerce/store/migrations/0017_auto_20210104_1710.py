# Generated by Django 3.1.4 on 2021-01-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210104_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='pic.JPG', null=True, upload_to=None),
        ),
    ]
