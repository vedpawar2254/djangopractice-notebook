# Generated by Django 4.0.4 on 2022-07-10 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0015_alter_test_title_alter_test_notes_test_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='notes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='base.notes'),
        ),
        migrations.AlterField(
            model_name='test_message',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='test_message',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_message', to='base.test'),
        ),
        migrations.AlterField(
            model_name='test_message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]