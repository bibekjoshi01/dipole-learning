# Generated by Django 4.1.5 on 2023-01-15 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_heading_sub_heading'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub_heading',
            options={'verbose_name': 'Sub Heading', 'verbose_name_plural': 'Sub Headings'},
        ),
    ]
