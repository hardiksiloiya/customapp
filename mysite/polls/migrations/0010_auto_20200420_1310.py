# Generated by Django 3.0.3 on 2020-04-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200416_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('family_type', models.CharField(max_length=10)),
                ('login', models.CharField(max_length=100)),
                ('ml_model', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='Question',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
