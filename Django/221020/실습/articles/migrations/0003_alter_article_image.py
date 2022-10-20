# Generated by Django 3.2.13 on 2022-10-20 09:10

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_art_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]
