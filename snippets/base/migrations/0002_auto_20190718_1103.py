# Generated by Django 2.2.2 on 2019-07-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_squashed_0097_asrsnippet_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetedcountry',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
