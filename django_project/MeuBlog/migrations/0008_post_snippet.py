# Generated by Django 3.2.5 on 2021-08-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeuBlog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click no link', max_length=255),
        ),
    ]