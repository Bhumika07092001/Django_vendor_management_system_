# Generated by Django 5.0.5 on 2024-05-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]