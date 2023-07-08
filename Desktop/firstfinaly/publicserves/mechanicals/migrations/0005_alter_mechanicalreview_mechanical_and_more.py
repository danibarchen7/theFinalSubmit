# Generated by Django 4.2.2 on 2023-07-08 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_transportscompany_pharmacies_mechanical_hospitals_and_more'),
        ('mechanicals', '0004_remove_mechanical_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanicalreview',
            name='mechanical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.mechanical'),
        ),
        migrations.AlterField(
            model_name='mechanicalwork',
            name='ip_m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.mechanical'),
        ),
        migrations.AlterField(
            model_name='mechanicservice',
            name='ip_m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.mechanical'),
        ),
        migrations.DeleteModel(
            name='Mechanical',
        ),
    ]
