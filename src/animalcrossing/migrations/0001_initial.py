# Generated by Django 2.2.2 on 2021-11-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('season', models.TextField()),
                ('location', models.TextField()),
                ('time', models.TextField()),
            ],
        ),
    ]
