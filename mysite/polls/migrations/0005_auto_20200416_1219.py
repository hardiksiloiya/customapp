# Generated by Django 3.0.3 on 2020-04-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200416_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
