# Generated by Django 4.2 on 2023-05-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0010_pharmacies_comments_pharmacies_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacies',
            name='picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
