# Generated by Django 2.2 on 2021-12-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]