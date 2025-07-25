# Generated by Django 4.2.16 on 2024-10-30 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VidTitle', models.CharField(max_length=300)),
                ('VidLink', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
    ]
