# Generated by Django 2.2.2 on 2019-06-30 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0003_auto_20190630_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auditlog',
            old_name='favourite_id',
            new_name='favourite',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='category_id',
            new_name='category',
        ),
    ]