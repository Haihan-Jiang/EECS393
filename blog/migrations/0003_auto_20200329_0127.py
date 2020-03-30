# Generated by Django 3.0.4 on 2020-03-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200329_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
