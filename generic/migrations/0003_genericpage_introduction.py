# Generated by Django 3.2.8 on 2021-10-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0002_alter_genericpage_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
    ]
