# Generated by Django 2.1.1 on 2019-03-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanBoard', '0002_auto_20190316_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Cardlistorder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
