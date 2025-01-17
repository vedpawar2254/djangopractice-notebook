# Generated by Django 4.0.4 on 2022-06-12 14:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(blank=True, max_length=150, null=True)),
                ('Notes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Summary', models.TextField(blank=True, max_length=750, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questions', models.TextField(blank=True, max_length=550, null=True)),
                ('Notes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notes')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=150, null=True)),
                ('Description', models.TextField(blank=True, max_length=250, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, default=None, related_name='post_note', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='note_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['updated', '-created'],
            },
        ),
        migrations.AddField(
            model_name='notes',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post'),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.URLField(blank=True, default='', max_length=350, null=True)),
                ('Notes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notes')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('like', 'like'), ('unlike', 'unlike')], default='like', max_length=10)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('dislike', 'dislike'), ('disunlike', 'disunlike')], default='dislike', max_length=10)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
