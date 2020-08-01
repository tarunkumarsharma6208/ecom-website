# Generated by Django 3.0.5 on 2020-05-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20200526_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
