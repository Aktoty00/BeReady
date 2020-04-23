# Generated by Django 2.2 on 2020-04-23 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='authAB_.Teacher'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='authAB_.Student'),
        ),
        migrations.AlterField(
            model_name='newsdiscussion',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstractPostDiscussion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsdiscussion',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsDiscussion_post', to='core.NewsPost'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentworkdiscussion',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentWorkDiscussion_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentworkdiscussion',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentWorkDiscussion_post', to='core.StudentWorkPost'),
        ),
        migrations.AlterField(
            model_name='studentworkpost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sw_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
