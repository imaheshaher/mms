# Generated by Django 3.1.7 on 2021-03-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210310_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]