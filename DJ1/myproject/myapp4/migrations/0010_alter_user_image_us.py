# Generated by Django 4.1.13 on 2024-04-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0009_alter_user_image_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_us',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
