# Generated by Django 4.2.7 on 2024-02-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_subcategory_userid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='item',
            new_name='maincategory',
        ),
    ]
