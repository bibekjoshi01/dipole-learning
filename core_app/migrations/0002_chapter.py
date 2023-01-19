# Generated by Django 4.1.5 on 2023-01-15 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='core_app.unit')),
            ],
        ),
    ]