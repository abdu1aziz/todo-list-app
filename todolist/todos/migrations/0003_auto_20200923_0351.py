# Generated by Django 3.1 on 2020-09-23 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_sharetodolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharetodolist',
            name='workList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='todos.worklist'),
        ),
    ]
