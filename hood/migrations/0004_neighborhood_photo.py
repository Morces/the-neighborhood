# Generated by Django 4.0 on 2022-06-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_rename_business_name_business_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
