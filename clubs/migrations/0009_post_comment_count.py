# Generated by Django 4.0.5 on 2022-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
