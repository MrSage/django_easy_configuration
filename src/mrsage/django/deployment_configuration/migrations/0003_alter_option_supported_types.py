# Generated by Django 4.2.9 on 2024-04-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployment_configuration', '0002_rename_value_option_raw_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='supported_types',
            field=models.ManyToManyField(related_name='supportedoptions', to='deployment_configuration.optiontype'),
        ),
    ]
