# Generated by Django 2.1.3 on 2018-11-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20181106_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
