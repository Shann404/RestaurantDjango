# Generated by Django 5.1.3 on 2024-11-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
