# Generated by Django 3.0.2 on 2020-01-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XRay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xRayImg', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
