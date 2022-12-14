# Generated by Django 4.1.3 on 2022-11-19 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_item_size_delete_sizevariant'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sizevariant'),
        ),
    ]
