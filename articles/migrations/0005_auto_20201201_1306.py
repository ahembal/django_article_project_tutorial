# Generated by Django 3.0 on 2020-12-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201201_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(default='drop-bear.jpg', upload_to='gallary'),
        ),
    ]
