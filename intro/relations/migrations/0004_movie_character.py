# Generated by Django 4.1.3 on 2022-11-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0003_language_alter_capital_name_alter_country_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('movies', models.ManyToManyField(to='relations.movie')),
            ],
        ),
    ]
