# Generated by Django 3.0.5 on 2020-06-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200526_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
