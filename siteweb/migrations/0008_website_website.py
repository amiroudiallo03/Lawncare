# Generated by Django 3.2.3 on 2021-05-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0007_delete_imagebanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='website',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
    ]
