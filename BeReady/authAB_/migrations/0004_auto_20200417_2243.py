# Generated by Django 2.1.7 on 2020-04-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAB_', '0003_auto_20200417_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stage',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], max_length=200),
        ),
    ]
