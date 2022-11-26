# Generated by Django 4.1.3 on 2022-11-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.IntegerField(choices=[(0, 'Pytanie'), (1, 'Inne')])),
                ('subject', models.CharField(max_length=64)),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]