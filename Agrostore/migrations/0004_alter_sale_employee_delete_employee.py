# Generated by Django 5.1.2 on 2024-11-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agrostore', '0003_task_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='employee',
            field=models.CharField(default='employee', max_length=150),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
