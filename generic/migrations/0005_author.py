# Generated by Django 3.2.8 on 2021-10-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_genericpage_banner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]