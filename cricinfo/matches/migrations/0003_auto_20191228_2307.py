# Generated by Django 3.0 on 2019-12-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20191219_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(choices=[('NOT STARTED', 'FIXTURE'), ('ON GOING', 'IN PROGRESS'), ('ABANDONED', 'ABANDONED'), ('--------------------', '---------------------'), ('Team Australia', 'Australia Won'), ('Team India', 'India Won'), ('Team Pakistan', 'Pakistan Won'), ('Team South Africa', 'South Africa Won'), ('Team Srilanka', 'Srilanka Won'), ('Team WestIndies', 'WestIndies Won'), ('Team England', 'England Won')], default='', max_length=100),
        ),
    ]
