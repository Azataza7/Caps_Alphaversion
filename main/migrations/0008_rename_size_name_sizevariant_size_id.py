# Generated by Django 4.1.3 on 2022-11-19 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_item_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sizevariant',
            old_name='size_name',
            new_name='size_id',
        ),
    ]
