# Generated by Django 3.1.3 on 2021-02-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
