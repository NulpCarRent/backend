# Generated by Django 3.0.7 on 2020-06-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=None, null=True)),
                ('client', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fines', to='api.Client')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
