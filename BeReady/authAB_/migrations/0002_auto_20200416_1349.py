# Generated by Django 2.1.7 on 2020-04-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAB_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stage',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], default='Freshman', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='level',
            field=models.CharField(choices=[('Associate degree', 'Associate degree'), ('Bachelor degree', 'Bachelor degree'), ('Master degree', 'Master degree'), ('Doctoral degree', 'Doctoral degree')], default='Associate degree', max_length=200),
        ),
    ]
