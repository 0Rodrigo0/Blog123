# Generated by Django 3.2.5 on 2021-09-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeuBlog', '0015_auto_20210918_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='static/MeuBlog/iamges/profile.jpg', null=True, upload_to='images/'),
        ),
    ]
