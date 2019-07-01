# Generated by Django 2.2.2 on 2019-07-01 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0013_delete_auditlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.TextField()),
                ('activity', models.TextField()),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to='favorites.Favorite')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
