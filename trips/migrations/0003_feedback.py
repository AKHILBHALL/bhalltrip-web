# Generated by Django 3.0.2 on 2020-01-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20200125_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
