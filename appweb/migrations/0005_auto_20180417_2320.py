# Generated by Django 2.0.4 on 2018-04-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_auto_20180417_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(null=True, verbose_name='Url page'),
        ),
        migrations.AlterField(
            model_name='company',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
