# Generated by Django 4.2.5 on 2024-02-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_user_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('price', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
