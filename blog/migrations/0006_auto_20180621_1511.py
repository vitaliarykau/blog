# Generated by Django 2.0.6 on 2018-06-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180621_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='user',
            new_name='authors',
        ),
    ]
