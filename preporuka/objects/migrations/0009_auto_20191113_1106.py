# Generated by Django 2.2.4 on 2019-11-13 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_auto_20191112_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='objects.City'),
        ),
    ]
