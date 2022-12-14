# Generated by Django 4.1.3 on 2022-11-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_sizevariant_alter_item_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/main'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ManyToManyField(blank=True, null=True, related_name='brand_id', to='main.brand'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(null=True, related_name='size_id', to='main.sizevariant'),
        ),
    ]
