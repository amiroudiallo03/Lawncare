# Generated by Django 3.2.3 on 2021-05-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0002_auto_20210520_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='image',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='website',
            name='adresse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='website',
            name='siteweb',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='website',
            name='titre_siteweb',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='website',
            name='titre_testimonial',
            field=models.CharField(max_length=100),
        ),
    ]
