# Generated by Django 2.1.5 on 2020-09-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200920_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
        ),
    ]
