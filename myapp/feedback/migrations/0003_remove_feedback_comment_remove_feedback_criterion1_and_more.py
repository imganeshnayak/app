# Generated by Django 4.1.13 on 2024-04-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_criterion1_alter_feedback_criterion2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion1',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion2',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion3',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion4',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion5',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion6',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='criterion7',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Feedback',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='batch',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='course',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='grading',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='section',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='semester',
            field=models.CharField(default='', max_length=100),
        ),
    ]
