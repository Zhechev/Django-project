# Generated by Django 2.2.4 on 2019-11-20 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0013_auto_20191119_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='author',
            field=models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, to='users.ProfileUser'),
        ),
    ]
