# Generated by Django 2.2.10 on 2020-06-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200527_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(default='photos/realtors/no-realtor.jpg', upload_to='photos/realtors'),
        ),
    ]
