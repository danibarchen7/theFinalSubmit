# Generated by Django 4.2 on 2023-05-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0015_alter_pharmacies_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacies',
            name='picture',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
