# Generated by Django 4.0.5 on 2022-07-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(choices=[('text', 'Text')], max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('posts', models.ManyToManyField(to='blog.post')),
            ],
        ),
    ]