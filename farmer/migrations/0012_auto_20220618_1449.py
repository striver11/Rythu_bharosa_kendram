# Generated by Django 3.2.12 on 2022-06-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0011_auto_20220618_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseagroproduct',
            name='status',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productstatus',
            name='title',
            field=models.CharField(default=1910673395, max_length=10, unique=True),
        ),
    ]
