# Generated by Django 3.0.3 on 2020-03-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200318_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='teachername',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
