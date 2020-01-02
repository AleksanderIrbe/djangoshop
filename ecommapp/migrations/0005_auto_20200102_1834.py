# Generated by Django 3.0 on 2020-01-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_auto_20191224_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='csrt_total',
            new_name='cart_total',
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecommapp.CartItem'),
        ),
    ]
