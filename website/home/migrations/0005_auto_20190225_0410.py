# Generated by Django 2.1.7 on 2019-02-25 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190225_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='000000', editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category'),
        ),
    ]
