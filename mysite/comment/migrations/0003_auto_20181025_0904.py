# Generated by Django 2.0 on 2018-10-25 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_auto_20181025_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='relpy_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='comment.Comment'),
        ),
    ]
