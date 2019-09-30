# Generated by Django 2.2.5 on 2019-09-30 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_auto_20190930_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armorycomponent',
            name='quote',
        ),
        migrations.AddField(
            model_name='armorycomponent',
            name='armory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.Armory'),
            preserve_default=False,
        ),
    ]