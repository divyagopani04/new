# Generated by Django 4.2.7 on 2024-02-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.CharField(default=0, max_length=100),
        ),
    ]