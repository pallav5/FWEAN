# Generated by Django 3.1.7 on 2021-04-05 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fweanapp.imagealbum')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]