# Generated by Django 2.2.5 on 2019-09-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190930_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armory',
            name='armory_components',
            field=models.ManyToManyField(related_name='armory_components', to='quotes.ArmoryComponent'),
        ),
    ]
