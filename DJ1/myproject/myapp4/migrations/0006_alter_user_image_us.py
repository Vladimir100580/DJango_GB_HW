# Generated by Django 4.1.13 on 2024-04-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0005_remove_user_image_user_image_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_us',
            field=models.ImageField(default=None, upload_to='./images/'),
        ),
    ]