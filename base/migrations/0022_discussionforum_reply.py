# Generated by Django 4.0.4 on 2022-07-19 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_discussionforum'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionforum',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='forum_reply', to='base.discussionforum'),
        ),
    ]