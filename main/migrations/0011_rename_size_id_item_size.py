# Generated by Django 4.1.3 on 2022-11-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_size_item_size_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='size_id',
            new_name='size',
        ),
    ]