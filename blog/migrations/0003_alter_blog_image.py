# Generated by Django 5.0.6 on 2024-06-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_like_blog_likes_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
