# Generated by Django 4.0.3 on 2022-03-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_todos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
