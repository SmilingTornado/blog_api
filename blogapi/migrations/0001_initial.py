# Generated by Django 3.0.6 on 2020-05-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
