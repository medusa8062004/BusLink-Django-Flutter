# Generated by Django 5.0 on 2023-12-29 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
            ],
        ),
    ]
