# Generated by Django 4.2.2 on 2023-06-23 08:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('ip_competence', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('competence', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('ip_h', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name_h', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('rating', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static\\PublicServes\\images')),
                ('site', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('ip_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.competence')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalType',
            fields=[
                ('ip_type', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField(default=django.utils.timezone.now)),
                ('rating', models.IntegerField()),
                ('ip_h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospitals')),
            ],
        ),
        migrations.AddField(
            model_name='hospitals',
            name='ip_t',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospitaltype'),
        ),
    ]
