# Generated by Django 4.2.7 on 2024-02-09 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_subcategory_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category',
            new_name='subitem',
        ),
    ]
