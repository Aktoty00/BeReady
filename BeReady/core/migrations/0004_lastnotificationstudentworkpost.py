# Generated by Django 2.2 on 2020-04-26 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_studentworkpost_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastNotificationStudentWorkPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_posts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.StudentWorkPost')),
            ],
            options={
                'verbose_name': 'LastNotificationStudentWorkPost',
                'verbose_name_plural': 'LastNotificationStudentWorkPosts',
            },
        ),
    ]
