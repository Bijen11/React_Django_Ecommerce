# Generated by Django 3.1.3 on 2021-03-31 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
