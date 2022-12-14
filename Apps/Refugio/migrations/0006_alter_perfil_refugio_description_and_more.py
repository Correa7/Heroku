# Generated by Django 4.1 on 2022-08-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Refugio', '0005_alter_perfil_refugio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_refugio',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='perfil_refugio',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='refugio_image/'),
        ),
        migrations.AlterField(
            model_name='perfil_refugio',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='refugio_image/'),
        ),
        migrations.AlterField(
            model_name='perfil_refugio',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='refugio_image/'),
        ),
        migrations.AlterField(
            model_name='perfil_refugio',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='refugio_image/'),
        ),
    ]
