# Generated by Django 3.0.5 on 2020-05-03 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20200502_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='more_personality',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='personal_exp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='special_needs',
            field=models.TextField(blank=True, null=True),
        ),
    ]