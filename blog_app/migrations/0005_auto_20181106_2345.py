# Generated by Django 2.1.3 on 2018-11-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20181106_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
