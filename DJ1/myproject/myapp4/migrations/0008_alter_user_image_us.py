# Generated by Django 4.1.13 on 2024-04-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0007_alter_user_image_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_us',
            field=models.ImageField(height_field=50, upload_to='images/', width_field=50),
        ),
    ]
